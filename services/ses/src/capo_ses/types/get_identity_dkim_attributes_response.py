"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityDkimAttributesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.dkim_attributes


class GetIdentityDkimAttributesResponse(TypedDict, closed=True):
    dkim_attributes: "capo_ses.types.dkim_attributes.DkimAttributes"
    """<p>The DKIM attributes for an email address or a domain.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityDkimAttributesResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.dkim_attributes

    capo_ses.types.dkim_attributes.serialize_query(
        value["dkim_attributes"], pairs, f"{key_prefix}DkimAttributes"
    )


def deserialize_query(el: Element) -> GetIdentityDkimAttributesResponse:
    out: GetIdentityDkimAttributesResponse = {}  # type: ignore[typeddict-item]
    child_dkim_attributes = el.find("DkimAttributes")
    if child_dkim_attributes is not None:
        import capo_ses.types.dkim_attributes

        out["dkim_attributes"] = capo_ses.types.dkim_attributes.deserialize_query(
            child_dkim_attributes
        )
    else:
        out["dkim_attributes"] = {}
    return out
