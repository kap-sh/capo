"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UpdateAppVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.additional_info_map
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version


class UpdateAppVersionResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>Resilience Hub application version.</p>"""
    additional_info: NotRequired[
        "capo_resiliencehub.types.additional_info_map.AdditionalInfoMap"
    ]
    """<p>Additional configuration parameters for an Resilience Hub application. If you want to implement <code>additionalInfo</code> through the Resilience Hub console rather than using an API call, see <a href="https://docs.aws.amazon.com/resilience-hub/latest/userguide/app-config-param.html">Configure the application configuration parameters</a>.</p> <note> <p>Currently, this parameter supports only failover region and account.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAppVersionResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    if "additional_info" in value:
        import capo_resiliencehub.types.additional_info_map

        out["additionalInfo"] = (
            capo_resiliencehub.types.additional_info_map.serialize_json(
                value["additional_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAppVersionResponse:
    out: UpdateAppVersionResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError("UpdateAppVersionResponse.app_arn required")
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError("UpdateAppVersionResponse.app_version required")
    if data.get("additionalInfo") is not None:
        import capo_resiliencehub.types.additional_info_map

        out["additional_info"] = (
            capo_resiliencehub.types.additional_info_map.deserialize_json(
                data["additionalInfo"]
            )
        )
    return out
