"""Generated from Smithy shape ``com.amazonaws.connect#ContactLensRedactionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_lens_redaction_entities_list
    import capo_connect.types.string


class ContactLensRedactionConfiguration(TypedDict, closed=True):
    behavior: NotRequired["capo_connect.types.string.String"]
    """<p>Specifies whether redaction is enabled for sensitive data, such as personal information, in the conversational analytics output. Valid values:</p> <ul> <li> <p> <code>Enable</code> – Redaction is applied according to the other values in this object.</p> </li> <li> <p> <code>Disable</code> – Redaction is not applied, and all other values in this object are ignored.</p> </li> </ul>"""
    policy: NotRequired["capo_connect.types.string.String"]
    """<p>The redaction policy that determines which versions of the transcript are stored. Valid values:</p> <ul> <li> <p> <code>None</code> – No redaction is applied.</p> </li> <li> <p> <code>RedactedOnly</code> – Only the redacted transcript is stored.</p> </li> <li> <p> <code>RedactedAndOriginal</code> – Both the redacted and the original transcript are stored.</p> </li> </ul>"""
    entities: NotRequired[
        "capo_connect.types.contact_lens_redaction_entities_list.ContactLensRedactionEntitiesList"
    ]
    """<p>The entity types to redact from the transcript (for example, <code>NAME</code>, <code>EMAIL</code>, <code>ADDRESS</code>).</p>"""
    mask_mode: NotRequired["capo_connect.types.string.String"]
    """<p>How sensitive information is masked in the transcript. Valid values:</p> <ul> <li> <p> <code>PII</code> – All redacted entities are replaced with the <code>[PII]</code> string.</p> </li> <li> <p> <code>EntityType</code> – All redacted entities are replaced with the label of the entity. For example, when the <code>EMAIL</code> entity is configured for redaction, emails in the transcript are replaced with the <code>[EMAIL]</code> string.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactLensRedactionConfiguration) -> dict:
    out: dict = {}
    if "behavior" in value:
        out["Behavior"] = value["behavior"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "entities" in value:
        import capo_connect.types.contact_lens_redaction_entities_list

        out["Entities"] = (
            capo_connect.types.contact_lens_redaction_entities_list.serialize_json(
                value["entities"]
            )
        )
    if "mask_mode" in value:
        out["MaskMode"] = value["mask_mode"]
    return out


def deserialize_json(data: dict) -> ContactLensRedactionConfiguration:
    out: ContactLensRedactionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        out["behavior"] = data["Behavior"]
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("Entities") is not None:
        import capo_connect.types.contact_lens_redaction_entities_list

        out["entities"] = (
            capo_connect.types.contact_lens_redaction_entities_list.deserialize_json(
                data["Entities"]
            )
        )
    if data.get("MaskMode") is not None:
        out["mask_mode"] = data["MaskMode"]
    return out
