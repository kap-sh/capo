"""Generated from Smithy shape ``com.amazonaws.appconfig#AccountSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.deletion_protection_settings
    import capo_appconfig.types.vended_metrics_settings


class AccountSettings(TypedDict, closed=True):
    deletion_protection: NotRequired[
        "capo_appconfig.types.deletion_protection_settings.DeletionProtectionSettings"
    ]
    """<p>A parameter to configure deletion protection. Deletion protection prevents a user from deleting a configuration profile or an environment if AppConfig has called either <a href="https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html">GetLatestConfiguration</a> or for the configuration profile or from the environment during the specified interval. The default interval for <code>ProtectionPeriodInMinutes</code> is 60.</p>"""
    vended_metrics: NotRequired[
        "capo_appconfig.types.vended_metrics_settings.VendedMetricsSettings"
    ]
    """<p>The configuration for vended metrics in the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccountSettings) -> dict:
    out: dict = {}
    if "deletion_protection" in value:
        import capo_appconfig.types.deletion_protection_settings

        out["DeletionProtection"] = (
            capo_appconfig.types.deletion_protection_settings.serialize_json(
                value["deletion_protection"]
            )
        )
    if "vended_metrics" in value:
        import capo_appconfig.types.vended_metrics_settings

        out["VendedMetrics"] = (
            capo_appconfig.types.vended_metrics_settings.serialize_json(
                value["vended_metrics"]
            )
        )
    return out


def deserialize_json(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if data.get("DeletionProtection") is not None:
        import capo_appconfig.types.deletion_protection_settings

        out["deletion_protection"] = (
            capo_appconfig.types.deletion_protection_settings.deserialize_json(
                data["DeletionProtection"]
            )
        )
    if data.get("VendedMetrics") is not None:
        import capo_appconfig.types.vended_metrics_settings

        out["vended_metrics"] = (
            capo_appconfig.types.vended_metrics_settings.deserialize_json(
                data["VendedMetrics"]
            )
        )
    return out
