"""Generated from Smithy shape ``com.amazonaws.support#TrustedAdvisorResourceDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.boolean
    import capo_support.types.string
    import capo_support.types.string_list


class TrustedAdvisorResourceDetail(TypedDict, closed=True):
    status: "capo_support.types.string.String"
    """<p>The status code for the resource identified in the Trusted Advisor check.</p>"""
    region: NotRequired["capo_support.types.string.String"]
    """<p>The Amazon Web Services Region in which the identified resource is located.</p>"""
    resource_id: "capo_support.types.string.String"
    """<p>The unique identifier for the identified resource.</p>"""
    is_suppressed: "capo_support.types.boolean.Boolean"
    """<p>Specifies whether the Amazon Web Services resource was ignored by Trusted Advisor because it was marked as suppressed by the user.</p>"""
    metadata: "capo_support.types.string_list.StringList"
    """<p>Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the <a>TrustedAdvisorCheckDescription</a> object returned by the call to <a>DescribeTrustedAdvisorChecks</a>. <b>Metadata</b> contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrustedAdvisorResourceDetail) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "region" in value:
        out["region"] = value["region"]
    out["resourceId"] = value["resource_id"]
    out["isSuppressed"] = value.get("is_suppressed", False)
    import capo_support.types.string_list

    out["metadata"] = capo_support.types.string_list.serialize_aws_json_1_1(
        value["metadata"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrustedAdvisorResourceDetail:
    out: TrustedAdvisorResourceDetail = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("region") is not None:
        out["region"] = data["region"]
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("isSuppressed") is not None:
        out["is_suppressed"] = data["isSuppressed"]
    else:
        out["is_suppressed"] = False
    if data.get("metadata") is not None:
        import capo_support.types.string_list

        out["metadata"] = capo_support.types.string_list.deserialize_aws_json_1_1(
            data["metadata"]
        )
    else:
        out["metadata"] = []
    return out
