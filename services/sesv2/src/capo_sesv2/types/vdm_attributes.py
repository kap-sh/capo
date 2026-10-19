"""Generated from Smithy shape ``com.amazonaws.sesv2#VdmAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.dashboard_attributes
    import capo_sesv2.types.feature_status
    import capo_sesv2.types.guardian_attributes


class VdmAttributes(TypedDict, closed=True):
    vdm_enabled: "capo_sesv2.types.feature_status.FeatureStatus"
    """<p>Specifies the status of your VDM configuration. Can be one of the following:</p> <ul> <li> <p> <code>ENABLED</code> – Amazon SES enables VDM for your account.</p> </li> <li> <p> <code>DISABLED</code> – Amazon SES disables VDM for your account.</p> </li> </ul>"""
    dashboard_attributes: NotRequired[
        "capo_sesv2.types.dashboard_attributes.DashboardAttributes"
    ]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Dashboard.</p>"""
    guardian_attributes: NotRequired[
        "capo_sesv2.types.guardian_attributes.GuardianAttributes"
    ]
    """<p>Specifies additional settings for your VDM configuration as applicable to the Guardian.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VdmAttributes) -> dict:
    out: dict = {}
    import capo_sesv2.types.feature_status

    out["VdmEnabled"] = capo_sesv2.types.feature_status.serialize_json(
        value["vdm_enabled"]
    )
    if "dashboard_attributes" in value:
        import capo_sesv2.types.dashboard_attributes

        out["DashboardAttributes"] = (
            capo_sesv2.types.dashboard_attributes.serialize_json(
                value["dashboard_attributes"]
            )
        )
    if "guardian_attributes" in value:
        import capo_sesv2.types.guardian_attributes

        out["GuardianAttributes"] = capo_sesv2.types.guardian_attributes.serialize_json(
            value["guardian_attributes"]
        )
    return out


def deserialize_json(data: dict) -> VdmAttributes:
    out: VdmAttributes = {}  # type: ignore[typeddict-item]
    if data.get("VdmEnabled") is not None:
        import capo_sesv2.types.feature_status

        out["vdm_enabled"] = capo_sesv2.types.feature_status.deserialize_json(
            data["VdmEnabled"]
        )
    else:
        import typing

        out["vdm_enabled"] = typing.cast(
            "capo_sesv2.types.feature_status.FeatureStatus", ""
        )
    if data.get("DashboardAttributes") is not None:
        import capo_sesv2.types.dashboard_attributes

        out["dashboard_attributes"] = (
            capo_sesv2.types.dashboard_attributes.deserialize_json(
                data["DashboardAttributes"]
            )
        )
    if data.get("GuardianAttributes") is not None:
        import capo_sesv2.types.guardian_attributes

        out["guardian_attributes"] = (
            capo_sesv2.types.guardian_attributes.deserialize_json(
                data["GuardianAttributes"]
            )
        )
    return out
