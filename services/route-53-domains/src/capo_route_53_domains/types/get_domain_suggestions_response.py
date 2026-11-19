"""Generated from Smithy shape ``com.amazonaws.route53domains#GetDomainSuggestionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route_53_domains.types.domain_suggestions_list


class GetDomainSuggestionsResponse(TypedDict, closed=True):
    suggestions_list: NotRequired[
        "capo_route_53_domains.types.domain_suggestions_list.DomainSuggestionsList"
    ]
    """<p>A list of possible domain names. If you specified <code>true</code> for <code>OnlyAvailable</code> in the request, the list contains only domains that are available for registration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDomainSuggestionsResponse) -> dict:
    out: dict = {}
    if "suggestions_list" in value:
        import capo_route_53_domains.types.domain_suggestions_list

        out["SuggestionsList"] = (
            capo_route_53_domains.types.domain_suggestions_list.serialize_aws_json_1_1(
                value["suggestions_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDomainSuggestionsResponse:
    out: GetDomainSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SuggestionsList") is not None:
        import capo_route_53_domains.types.domain_suggestions_list

        out["suggestions_list"] = (
            capo_route_53_domains.types.domain_suggestions_list.deserialize_aws_json_1_1(
                data["SuggestionsList"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetDomainSuggestionsResponse) -> dict:
    out: dict = {}
    if "suggestions_list" in value:
        import capo_route_53_domains.types.domain_suggestions_list

        out["SuggestionsList"] = (
            capo_route_53_domains.types.domain_suggestions_list.serialize_cbor(
                value["suggestions_list"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> GetDomainSuggestionsResponse:
    out: GetDomainSuggestionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("SuggestionsList") is not None:
        import capo_route_53_domains.types.domain_suggestions_list

        out["suggestions_list"] = (
            capo_route_53_domains.types.domain_suggestions_list.deserialize_cbor(
                data["SuggestionsList"]
            )
        )
    return out
