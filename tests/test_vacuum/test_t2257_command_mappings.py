"""Tests for T2257 command mappings and DPS codes."""

import pytest
from typing import Any
from unittest.mock import patch

from custom_components.robovac.robovac import RoboVac
from custom_components.robovac.vacuums.base import RobovacCommand


@pytest.fixture
def mock_T2257_robovac() -> RoboVac:
    """Create a mock T2257 RoboVac instance for testing."""
    with patch("custom_components.robovac.robovac.TuyaDevice.__init__", return_value=None):
        robovac = RoboVac(
            model_code="T2257",
            device_id="test_id",
            host="192.168.1.100",
            local_key="test_key",
        )
        return robovac


def test_T2257_mode_command_values(mock_T2257_robovac) -> None:
    """Test T2257 MODE command value mappings."""
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "auto") == "Auto"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "small_room") == "SmallRoom"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "spot") == "Spot"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "edge") == "Edge"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "nosweep") == "Nosweep"

    # Unknown returns as-is
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.MODE, "unknown") == "unknown"


def test_T2257_mode_case_insensitive(mock_T2257_robovac) -> None:
    """Test T2257 MODE command accepts case-insensitive values via getRoboVacHumanReadableValue."""
    # Case-insensitive matching should work for device responses
    assert mock_T2257_robovac.getRoboVacHumanReadableValue(RobovacCommand.MODE, "auto") == "Auto"
    assert mock_T2257_robovac.getRoboVacHumanReadableValue(RobovacCommand.MODE, "Auto") == "Auto"
    assert mock_T2257_robovac.getRoboVacHumanReadableValue(RobovacCommand.MODE, "AUTO") == "Auto"


def test_T2257_fan_speed_command_values(mock_T2257_robovac) -> None:
    """Test T2257 FAN_SPEED value mapping."""
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "standard") == "Standard"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "turbo") == "Turbo"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "max") == "Max"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "boost_iq") == "Boost_IQ"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "quiet") == "Quiet"
    assert mock_T2257_robovac.getRoboVacCommandValue(RobovacCommand.FAN_SPEED, "unknown") == "unknown"


def test_T2257_error_code_mapping(mock_T2257_robovac) -> None:
    """Test T2257 error code 0 maps to 'No error'."""
    assert mock_T2257_robovac.getRoboVacHumanReadableValue(RobovacCommand.ERROR, "0") == "No error"


def test_T2257_model_has_commands(mock_T2257_robovac) -> None:
    """Test that T2257 model has required commands defined."""
    commands = mock_T2257_robovac.model_details.commands

    assert RobovacCommand.MODE in commands
    assert RobovacCommand.STATUS in commands
    assert RobovacCommand.RETURN_HOME in commands
    assert RobovacCommand.FAN_SPEED in commands
    assert RobovacCommand.LOCATE in commands
    assert RobovacCommand.BATTERY in commands
    assert RobovacCommand.ERROR in commands
    assert RobovacCommand.BOOST_IQ in commands
    assert RobovacCommand.AUTO_RETURN in commands
