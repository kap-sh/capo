"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ListCalculatedAttributeDefinitionsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.calculated_attribute_definitions_list
    import capo_customer_profiles.types.token


class ListCalculatedAttributeDefinitionsResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_customer_profiles.types.calculated_attribute_definitions_list.CalculatedAttributeDefinitionsList"
    ]
    """<p>The list of calculated attribute definitions.</p>"""
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous call to ListCalculatedAttributeDefinitions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCalculatedAttributeDefinitionsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_customer_profiles.types.calculated_attribute_definitions_list

        out["Items"] = (
            capo_customer_profiles.types.calculated_attribute_definitions_list.serialize_json(
                value["items"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCalculatedAttributeDefinitionsResponse:
    out: ListCalculatedAttributeDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("Items") is not None:
        import capo_customer_profiles.types.calculated_attribute_definitions_list

        out["items"] = (
            capo_customer_profiles.types.calculated_attribute_definitions_list.deserialize_json(
                data["Items"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


def redact_sensitive(
    value: ListCalculatedAttributeDefinitionsResponse,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        out["items"] = "*** Sensitive Data Redacted ***"
    return out
