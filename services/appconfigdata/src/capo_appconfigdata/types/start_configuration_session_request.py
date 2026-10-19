"""Generated from Smithy shape ``com.amazonaws.appconfigdata#StartConfigurationSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfigdata.types.identifier
    import capo_appconfigdata.types.optional_poll_seconds


class StartConfigurationSessionRequest(TypedDict, closed=True):
    application_identifier: "capo_appconfigdata.types.identifier.Identifier"
    """<p>The application ID or the application name.</p>"""
    environment_identifier: "capo_appconfigdata.types.identifier.Identifier"
    """<p>The environment ID or the environment name.</p>"""
    configuration_profile_identifier: "capo_appconfigdata.types.identifier.Identifier"
    """<p>The configuration profile ID or the configuration profile name.</p>"""
    required_minimum_poll_interval_in_seconds: NotRequired[
        "capo_appconfigdata.types.optional_poll_seconds.OptionalPollSeconds"
    ]
    """<p>Sets a constraint on a session. If you specify a value of, for example, 60 seconds, then the client that established the session can't call <a>GetLatestConfiguration</a> more frequently than every 60 seconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartConfigurationSessionRequest) -> dict:
    out: dict = {}
    out["ApplicationIdentifier"] = value["application_identifier"]
    out["EnvironmentIdentifier"] = value["environment_identifier"]
    out["ConfigurationProfileIdentifier"] = value["configuration_profile_identifier"]
    if "required_minimum_poll_interval_in_seconds" in value:
        out["RequiredMinimumPollIntervalInSeconds"] = value[
            "required_minimum_poll_interval_in_seconds"
        ]
    return out


def deserialize_json(data: dict) -> StartConfigurationSessionRequest:
    out: StartConfigurationSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationIdentifier") is not None:
        out["application_identifier"] = data["ApplicationIdentifier"]
    else:
        out["application_identifier"] = ""
    if data.get("EnvironmentIdentifier") is not None:
        out["environment_identifier"] = data["EnvironmentIdentifier"]
    else:
        out["environment_identifier"] = ""
    if data.get("ConfigurationProfileIdentifier") is not None:
        out["configuration_profile_identifier"] = data["ConfigurationProfileIdentifier"]
    else:
        out["configuration_profile_identifier"] = ""
    if data.get("RequiredMinimumPollIntervalInSeconds") is not None:
        out["required_minimum_poll_interval_in_seconds"] = data[
            "RequiredMinimumPollIntervalInSeconds"
        ]
    return out
