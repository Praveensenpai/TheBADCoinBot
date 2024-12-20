import asyncio
from contextlib import suppress
from datetime import timedelta
import random
import time
import traceback

import humanize
from badcoin.bad import BAD
from badcoin.models import UserInfo
from env import Env
from telegram.client import TGClient
from utils.dt import human_readable
from utils.loggy import logger
from utils.pre_verify import pre_verify


class TheBADCoinBot:
    def calculate_total_taps(self, user_info: UserInfo) -> int:
        available_energy = user_info.user.tapping.available
        action_energy = user_info.user.tapping.action_energy
        if action_energy == 0 or available_energy < action_energy:
            return 0
        taps = (available_energy + action_energy - 1) // action_energy
        return taps

    def __humanize_number(self, number: int) -> str:
        return humanize.naturalsize(number, gnu=True, format="%.3f")

    def hold_task(self, bad: BAD, user_info: UserInfo) -> None:
        logger.info(f"User ID: {user_info.user.id}")
        logger.info(f"Balance: {self.__humanize_number(user_info.user.balance)}")
        logger.info(f"Holding Energy Available: {user_info.user.holding.available}")

        if user_info.user.holding.available < 1:
            logger.info("No Holding Energy Available.")
            return
        for play_count in range(user_info.user.holding.available):
            logger.info(
                f"[{play_count + 1}/{user_info.user.holding.available}] Starting Holding"
            )
            start_info = bad.hold_start()
            holding_checkpoint: int = 0
            hold_target = random.randint(Env.MIN_HOLD, Env.MAX_HOLD)
            logger.info(f"Target Holding Checkpoint: {hold_target}")

            for i in range(1, hold_target + 1):
                check_info = bad.hold_check(i, start_info.holding_token)
                if not check_info.holding_success:
                    logger.info(f"Holding Checkpoint {i} Failed.")
                    logger.warning(
                        f"[{play_count + 1}/{user_info.user.holding.available}] Holding Failed"
                    )
                    break
                logger.info(f"Holding Checkpoint {i} Successful.")
                time.sleep(1)
                holding_checkpoint = i

            else:
                logger.success("All Holding Checkpoints Passed!")
                claim_info = bad.hold_claim(
                    holding_checkpoint, start_info.holding_token
                )
                logger.success("Holding Claim Successful!")
                logger.success(
                    f"Reward Earned: {self.__humanize_number(claim_info.reward.balance)}"
                )
                logger.success(
                    f"[{play_count + 1}/{user_info.user.holding.available}] Completed Holding"
                )

            sleep_delay = random.randint(5, 10)
            logger.info(f"Waiting {sleep_delay} seconds before next hold.")
            time.sleep(sleep_delay)

    def tap_task(self, bad: BAD, user_info: UserInfo) -> None:
        logger.info(f"User ID: {user_info.user.id}")
        logger.info(f"Balance: {self.__humanize_number(user_info.user.balance)}")
        logger.info(f"Energy Available: {user_info.user.tapping.available}")
        total_taps = self.calculate_total_taps(user_info)
        logger.info(f"Total Taps Available: {total_taps}")
        for _ in range(total_taps):
            try:
                tap_info = bad.tap()
                logger.success("Tap Successful")
                logger.info(
                    f"Energy Available After Tap: {tap_info.user.tapping.available}"
                )
                logger.info(
                    f"Balance: {self.__humanize_number(user_info.user.balance)}"
                )
                if (
                    tap_info.user.tapping.available
                    < tap_info.user.tapping.action_energy
                ):
                    logger.warning("Not enough Energy to tap.")
                    break

                sleep_delay = random.randint(5, 10)
                logger.info(f"Waiting {sleep_delay} seconds before next tap.")
                time.sleep(sleep_delay)
            except Exception as e:
                logger.error(f"Tap Failed: {e}")
                logger.error(traceback.format_exc())
                logger.info("Let's wait for 5 minutes before retrying.")
                time.sleep(60 * 5)

    async def main(self):
        sleep_delay = Env.SLEEP_DELAY_MINUTES
        logger.info(f"SLEEP DELAY SET TO {sleep_delay} MINUTES")
        while True:
            try:
                client = TGClient()
                query = await client.get_query_string("BadCoinBadBot", "app")
                bad = BAD(query)
                user_info = bad.info()
                bad.create()
                self.tap_task(bad, user_info)
                self.hold_task(bad, user_info)
                rest_period = 60 * sleep_delay
                logger.info(
                    f"Lets take a rest for {human_readable(timedelta(seconds=rest_period))}"
                )
                await asyncio.sleep(rest_period)
            except Exception as e:
                logger.error(f"An unexpected error occurred: {e}")
                logger.error(traceback.format_exc())
                logger.info("Let's take a 60 minutes break.")
                await asyncio.sleep(60 * 60)

    def run(self):
        pre_verify()
        while True:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            try:
                loop.run_until_complete(self.main())
            except Exception as e:
                logger.error(traceback.format_exc())
                logger.error(f"Restarting event loop due to error: {e}")
            finally:
                with suppress(Exception):
                    loop.close()
                logger.info("Restarting the main loop...")
                time.sleep(10)


if __name__ == "__main__":
    TheBADCoinBot().run()
