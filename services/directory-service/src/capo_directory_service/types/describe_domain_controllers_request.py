"""Generated from Smithy shape ``com.amazonaws.directoryservice#DescribeDomainControllersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.domain_controller_ids
    import capo_directory_service.types.limit
    import capo_directory_service.types.next_token


class DescribeDomainControllersRequest(TypedDict, closed=True):
    directory_id: "capo_directory_service.types.directory_id.DirectoryId"
    """<p>Identifier of the directory for which to retrieve the domain controller information.</p>"""
    domain_controller_ids: NotRequired[
        "capo_directory_service.types.domain_controller_ids.DomainControllerIds"
    ]
    """<p>A list of identifiers for the domain controllers whose information will be provided.</p>"""
    next_token: NotRequired["capo_directory_service.types.next_token.NextToken"]
    """<p>The <i>DescribeDomainControllers.NextToken</i> value from a previous call to <a>DescribeDomainControllers</a>. Pass null if this is the first call. </p>"""
    limit: NotRequired["capo_directory_service.types.limit.Limit"]
    """<p>The maximum number of items to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDomainControllersRequest) -> dict:
    out: dict = {}
    out["DirectoryId"] = value["directory_id"]
    if "domain_controller_ids" in value:
        import capo_directory_service.types.domain_controller_ids

        out["DomainControllerIds"] = (
            capo_directory_service.types.domain_controller_ids.serialize_aws_json_1_1(
                value["domain_controller_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDomainControllersRequest:
    out: DescribeDomainControllersRequest = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    else:
        out["directory_id"] = ""
    if data.get("DomainControllerIds") is not None:
        import capo_directory_service.types.domain_controller_ids

        out["domain_controller_ids"] = (
            capo_directory_service.types.domain_controller_ids.deserialize_aws_json_1_1(
                data["DomainControllerIds"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
