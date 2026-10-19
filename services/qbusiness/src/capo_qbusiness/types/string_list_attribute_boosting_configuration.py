"""Generated from Smithy shape ``com.amazonaws.qbusiness#StringListAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_boosting_level


class StringListAttributeBoostingConfiguration(TypedDict, closed=True):
    boosting_level: "capo_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel"
    """<p>Specifies the priority of boosted document attributes in relation to other boosted attributes. This parameter determines how strongly the attribute influences document ranking in search results. <code>STRING_LIST</code> attributes can serve as additional boosting factors when needed, but are not supported when using <code>NativeIndexConfiguration</code> version 2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringListAttributeBoostingConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.document_attribute_boosting_level

    out["boostingLevel"] = (
        capo_qbusiness.types.document_attribute_boosting_level.serialize_json(
            value["boosting_level"]
        )
    )
    return out


def deserialize_json(data: dict) -> StringListAttributeBoostingConfiguration:
    out: StringListAttributeBoostingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("boostingLevel") is not None:
        import capo_qbusiness.types.document_attribute_boosting_level

        out["boosting_level"] = (
            capo_qbusiness.types.document_attribute_boosting_level.deserialize_json(
                data["boostingLevel"]
            )
        )
    else:
        import typing

        out["boosting_level"] = typing.cast(
            "capo_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel",
            "",
        )
    return out
