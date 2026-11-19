"""Generated from Smithy shape ``com.amazonaws.appstream#ListEntitledApplicationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.entitled_application_list
    import capo_appstream.types.string


class ListEntitledApplicationsResult(TypedDict, closed=True):
    entitled_applications: NotRequired[
        "capo_appstream.types.entitled_application_list.EntitledApplicationList"
    ]
    """<p>The entitled applications.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEntitledApplicationsResult) -> dict:
    out: dict = {}
    if "entitled_applications" in value:
        import capo_appstream.types.entitled_application_list

        out["EntitledApplications"] = (
            capo_appstream.types.entitled_application_list.serialize_aws_json_1_1(
                value["entitled_applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEntitledApplicationsResult:
    out: ListEntitledApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("EntitledApplications") is not None:
        import capo_appstream.types.entitled_application_list

        out["entitled_applications"] = (
            capo_appstream.types.entitled_application_list.deserialize_aws_json_1_1(
                data["EntitledApplications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEntitledApplicationsResult) -> dict:
    out: dict = {}
    if "entitled_applications" in value:
        import capo_appstream.types.entitled_application_list

        out["EntitledApplications"] = (
            capo_appstream.types.entitled_application_list.serialize_cbor(
                value["entitled_applications"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListEntitledApplicationsResult:
    out: ListEntitledApplicationsResult = {}  # type: ignore[typeddict-item]
    if data.get("EntitledApplications") is not None:
        import capo_appstream.types.entitled_application_list

        out["entitled_applications"] = (
            capo_appstream.types.entitled_application_list.deserialize_cbor(
                data["EntitledApplications"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
