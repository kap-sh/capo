"""Generated from Smithy shape ``com.amazonaws.ses#GetIdentityVerificationAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.identity_list


class GetIdentityVerificationAttributesRequest(TypedDict, closed=True):
    identities: "capo_ses.types.identity_list.IdentityList"
    """<p>A list of identities.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetIdentityVerificationAttributesRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.identity_list

    capo_ses.types.identity_list.serialize_query(
        value["identities"], pairs, f"{key_prefix}Identities"
    )


def deserialize_query(el: Element) -> GetIdentityVerificationAttributesRequest:
    out: GetIdentityVerificationAttributesRequest = {}  # type: ignore[typeddict-item]
    child_identities = el.find("Identities")
    if child_identities is not None:
        import capo_ses.types.identity_list

        out["identities"] = capo_ses.types.identity_list.deserialize_query(
            child_identities
        )
    else:
        out["identities"] = []
    return out
