"""Generated from Smithy shape ``com.amazonaws.workmail#ListResourcesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workmail.types.next_token
    import capo_workmail.types.resources


class ListResourcesResponse(TypedDict, closed=True):
    resources: NotRequired["capo_workmail.types.resources.Resources"]
    """<p>One page of the organization's resource representation.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p> The token used to paginate through all the organization's resources. While results are still available, it has an associated value. When the last page is reached, the token is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesResponse) -> dict:
    out: dict = {}
    if "resources" in value:
        import capo_workmail.types.resources

        out["Resources"] = capo_workmail.types.resources.serialize_aws_json_1_1(
            value["resources"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesResponse:
    out: ListResourcesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Resources") is not None:
        import capo_workmail.types.resources

        out["resources"] = capo_workmail.types.resources.deserialize_aws_json_1_1(
            data["Resources"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListResourcesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "resources" in value:
        import capo_workmail.types.resources

        out["resources"] = capo_workmail.types.resources.redact_sensitive(
            value["resources"]
        )
    return out
