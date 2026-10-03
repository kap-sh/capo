"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DescribeDraftAppVersionResourcesImportStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.entity_version
    import capo_resiliencehub.types.error_detail_list
    import capo_resiliencehub.types.resource_import_status_type
    import capo_resiliencehub.types.string500
    import capo_resiliencehub.types.time_stamp


class DescribeDraftAppVersionResourcesImportStatusResponse(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    app_version: "capo_resiliencehub.types.entity_version.EntityVersion"
    """<p>The version of the application.</p>"""
    status: (
        "capo_resiliencehub.types.resource_import_status_type.ResourceImportStatusType"
    )
    """<p>Status of the action.</p>"""
    status_change_time: "capo_resiliencehub.types.time_stamp.TimeStamp"
    """<p>The time when the status last changed.</p>"""
    error_message: NotRequired["capo_resiliencehub.types.string500.String500"]
    """<p>The error message returned for the resource request.</p>"""
    error_details: NotRequired[
        "capo_resiliencehub.types.error_detail_list.ErrorDetailList"
    ]
    """<p>List of errors that were encountered while importing resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDraftAppVersionResourcesImportStatusResponse) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    out["appVersion"] = value["app_version"]
    import capo_resiliencehub.types.resource_import_status_type

    out["status"] = capo_resiliencehub.types.resource_import_status_type.serialize_json(
        value["status"]
    )
    import capo_resiliencehub.types.time_stamp

    out["statusChangeTime"] = capo_resiliencehub.types.time_stamp.serialize_json(
        value["status_change_time"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_details" in value:
        import capo_resiliencehub.types.error_detail_list

        out["errorDetails"] = capo_resiliencehub.types.error_detail_list.serialize_json(
            value["error_details"]
        )
    return out


def deserialize_json(
    data: dict,
) -> DescribeDraftAppVersionResourcesImportStatusResponse:
    out: DescribeDraftAppVersionResourcesImportStatusResponse = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.app_arn required"
        )
    if data.get("appVersion") is not None:
        out["app_version"] = data["appVersion"]
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.app_version required"
        )
    if data.get("status") is not None:
        import capo_resiliencehub.types.resource_import_status_type

        out["status"] = (
            capo_resiliencehub.types.resource_import_status_type.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.status required"
        )
    if data.get("statusChangeTime") is not None:
        import capo_resiliencehub.types.time_stamp

        out["status_change_time"] = (
            capo_resiliencehub.types.time_stamp.deserialize_json(
                data["statusChangeTime"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeDraftAppVersionResourcesImportStatusResponse.status_change_time required"
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    if data.get("errorDetails") is not None:
        import capo_resiliencehub.types.error_detail_list

        out["error_details"] = (
            capo_resiliencehub.types.error_detail_list.deserialize_json(
                data["errorDetails"]
            )
        )
    return out
