"""Generated from Smithy shape ``com.amazonaws.appconfig#DeletionProtectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.boolean
    import capo_appconfig.types.deletion_protection_duration


class DeletionProtectionSettings(TypedDict, closed=True):
    enabled: NotRequired["capo_appconfig.types.boolean.Boolean"]
    """<p>A parameter that indicates if deletion protection is enabled or not.</p>"""
    protection_period_in_minutes: NotRequired[
        "capo_appconfig.types.deletion_protection_duration.DeletionProtectionDuration"
    ]
    """<p>The time interval during which AppConfig monitors for calls to <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> or for a configuration profile or from an environment. AppConfig returns an error if a user calls or for the designated configuration profile or environment. To bypass the error and delete a configuration profile or an environment, specify <code>BYPASS</code> for the <code>DeletionProtectionCheck</code> parameter for either or .</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletionProtectionSettings) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "protection_period_in_minutes" in value:
        out["ProtectionPeriodInMinutes"] = value["protection_period_in_minutes"]
    return out


def deserialize_json(data: dict) -> DeletionProtectionSettings:
    out: DeletionProtectionSettings = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("ProtectionPeriodInMinutes") is not None:
        out["protection_period_in_minutes"] = data["ProtectionPeriodInMinutes"]
    return out
