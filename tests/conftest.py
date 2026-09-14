from copy import deepcopy

import pytest

from src import app as app_module


initial_activities = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = deepcopy(initial_activities)