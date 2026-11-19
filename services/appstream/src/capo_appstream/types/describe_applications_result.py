"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.applications
    import capo_appstream.types.string


class DescribeApplicationsResult(TypedDict, closed=True):
    applications: NotRequired["capo_appstream.types.applications.Applications"]
    """<p>The applications in the list.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeApplicationsResult) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_appstream.types.applications

        out["Applications"] = capo_appstream.types.applications.serialize_aws_json_1_1(
            value["applications"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeApplicationsResult:
    out: DescribeApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Applications") is not None:
        import capo_appstream.types.applications

        out["applications"] = (
            capo_appstream.types.applications.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeApplicationsResult) -> dict:
    out: dict = {}
    if "applications" in value:
        import capo_appstream.types.applications

        out["Applications"] = capo_appstream.types.applications.serialize_cbor(
            value["applications"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeApplicationsResult:
    out: DescribeApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("Applications") is not None:
        import capo_appstream.types.applications

        out["applications"] = capo_appstream.types.applications.deserialize_cbor(
            data["Applications"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
