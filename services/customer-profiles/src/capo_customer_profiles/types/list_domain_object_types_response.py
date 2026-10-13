"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListDomainObjectTypesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.domain_object_types_list
    import capo_customer_profiles.types.token


class ListDomainObjectTypesResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_customer_profiles.types.domain_object_types_list.DomainObjectTypesList"
    ]
    """<p>The list of domain object types.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListDomainObjectTypes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainObjectTypesResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.domain_object_types_list

        out["Items"] = (
            capo_customer_profiles.types.domain_object_types_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainObjectTypesResponse:
    out: ListDomainObjectTypesResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_customer_profiles.types.domain_object_types_list

        out["items"] = (
            capo_customer_profiles.types.domain_object_types_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(value: ListDomainObjectTypesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        out["items"] = "*** Sensitive Data Redacted ***"
    return out
