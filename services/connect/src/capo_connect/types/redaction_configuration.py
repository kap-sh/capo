"""Generated from Smithy shape ``com.amazonaws.connect#RedactionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.behavior
    import capo_connect.types.entities
    import capo_connect.types.mask_mode
    import capo_connect.types.policy


class RedactionConfiguration(TypedDict, closed=True):
    behavior: "capo_connect.types.behavior.Behavior"
    """<p>Controls whether redaction is applied to the analytics output. Valid values: <code>Enable</code> | <code>Disable</code>.</p>"""
    policy: "capo_connect.types.policy.Policy"
    """<p>The redaction output policy that determines which versions of the transcript are stored. Valid values: <code>None</code> | <code>RedactedOnly</code> | <code>RedactedAndOriginal</code>.</p>"""
    entities: NotRequired["capo_connect.types.entities.Entities"]
    """<p>The list of PII entity types to redact from the transcript (for example, <code>NAME</code>, <code>ADDRESS</code>, <code>CREDIT_DEBIT_NUMBER</code>).</p>"""
    mask_mode: NotRequired["capo_connect.types.mask_mode.MaskMode"]
    """<p>The masking mode that determines how redacted content is replaced in the output. Valid values: <code>PII</code> (replaces with the literal string [PII]) | <code>EntityType</code> (replaces with the entity type name, for example [NAME]).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactionConfiguration) -> dict:
    out: dict = {}
    import capo_connect.types.behavior

    out["Behavior"] = capo_connect.types.behavior.serialize_json(value["behavior"])
    import capo_connect.types.policy

    out["Policy"] = capo_connect.types.policy.serialize_json(value["policy"])
    if "entities" in value:
        import capo_connect.types.entities

        out["Entities"] = capo_connect.types.entities.serialize_json(value["entities"])
    if "mask_mode" in value:
        import capo_connect.types.mask_mode

        out["MaskMode"] = capo_connect.types.mask_mode.serialize_json(
            value["mask_mode"]
        )
    return out


def deserialize_json(data: dict) -> RedactionConfiguration:
    out: RedactionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Behavior") is not None:
        import capo_connect.types.behavior

        out["behavior"] = capo_connect.types.behavior.deserialize_json(data["Behavior"])
    else:
        import typing

        out["behavior"] = typing.cast("capo_connect.types.behavior.Behavior", "")
    if data.get("Policy") is not None:
        import capo_connect.types.policy

        out["policy"] = capo_connect.types.policy.deserialize_json(data["Policy"])
    else:
        import typing

        out["policy"] = typing.cast("capo_connect.types.policy.Policy", "")
    if data.get("Entities") is not None:
        import capo_connect.types.entities

        out["entities"] = capo_connect.types.entities.deserialize_json(data["Entities"])
    if data.get("MaskMode") is not None:
        import capo_connect.types.mask_mode

        out["mask_mode"] = capo_connect.types.mask_mode.deserialize_json(
            data["MaskMode"]
        )
    return out
