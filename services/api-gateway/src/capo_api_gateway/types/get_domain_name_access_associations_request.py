"""Generated from Smithy shape ``com.amazonaws.apigateway#GetDomainNameAccessAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_api_gateway.types.nullable_integer
    import capo_api_gateway.types.resource_owner
    import capo_api_gateway.types.string


class GetDomainNameAccessAssociationsRequest(TypedDict, closed=True):
    position: NotRequired["capo_api_gateway.types.string.String"]
    """<p>The current pagination position in the paged result set. </p>"""
    limit: NotRequired["capo_api_gateway.types.nullable_integer.NullableInteger"]
    """<p>The maximum number of returned results per page. The default value is 25 and the maximum value is 500. </p>"""
    resource_owner: NotRequired["capo_api_gateway.types.resource_owner.ResourceOwner"]
    """<p> The owner of the domain name access association. Use <code>SELF</code> to only list the domain name access associations owned by your own account. Use <code>OTHER_ACCOUNTS</code> to list the domain name access associations with your private custom domain names that are owned by other Amazon Web Services accounts.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDomainNameAccessAssociationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDomainNameAccessAssociationsRequest:
    out: GetDomainNameAccessAssociationsRequest = {}  # type: ignore[typeddict-item]
    return out
