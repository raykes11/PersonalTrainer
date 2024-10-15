from aiogram import Router

from action.set_machine import router as set_machine
from action.start_trening import router as start_trening
from base_command import router as base_command
from registration.exercise_machine import router as exercise_machine
from registration.trainers import router as trainers
from registration.user import router as user

router = Router()
router.include_router(base_command)
router.include_router(exercise_machine)
router.include_router(trainers)
router.include_router(user)
router.include_router(set_machine)
router.include_router(start_trening)
