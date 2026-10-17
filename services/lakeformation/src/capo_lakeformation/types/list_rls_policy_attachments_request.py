"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListRLSPolicyAttachmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.page_size
    import capo_lakeformation.types.resource
    import capo_lakeformation.types.token


class ListRLSPolicyAttachmentsRequest(TypedDict, closed=True):
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>If specified, returns only the attachments for the given resource.</p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>If specified, returns only the attachments for the given principal.</p>"""
    policy_name: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>If specified, returns only the attachments for the row-level security policy with this name.</p>"""
    max_results: NotRequired["capo_lakeformation.types.page_size.PageSize"]
    """<p>The maximum number of attachments to return in a single response.</p>"""
    next_token: NotRequired["capo_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRLSPolicyAttachmentsRequest) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "policy_name" in value:
        out["PolicyName"] = value["policy_name"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRLSPolicyAttachmentsRequest:
    out: ListRLSPolicyAttachmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if data.get("Principal") is not None:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if data.get("PolicyName") is not None:
        out["policy_name"] = data["PolicyName"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
