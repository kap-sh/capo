"""Generated from Smithy shape ``com.amazonaws.qbusiness#DateAttributeBoostingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.boosting_duration_in_seconds
    import capo_qbusiness.types.document_attribute_boosting_level


class DateAttributeBoostingConfiguration(TypedDict, closed=True):
    boosting_level: "capo_qbusiness.types.document_attribute_boosting_level.DocumentAttributeBoostingLevel"
    """<p>Specifies the priority tier ranking of boosting applied to document attributes. For version 2, this parameter indicates the relative ranking between boosted fields (ONE being highest priority, TWO being second highest, etc.) and determines the order in which attributes influence document ranking in search results. For version 1, this parameter specifies the boosting intensity. For version 2, boosting intensity (VERY HIGH, HIGH, MEDIUM, LOW, NONE) are not supported. Note that in version 2, you are not allowed to boost on only one field and make this value TWO.</p>"""
    boosting_duration_in_seconds: NotRequired[
        "capo_qbusiness.types.boosting_duration_in_seconds.BoostingDurationInSeconds"
    ]
    """<p>Specifies the duration, in seconds, of a boost applies to a <code>DATE</code> type document attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateAttributeBoostingConfiguration) -> dict:
    out: dict = {}
    import capo_qbusiness.types.document_attribute_boosting_level

    out["boostingLevel"] = (
        capo_qbusiness.types.document_attribute_boosting_level.serialize_json(
            value["boosting_level"]
        )
    )
    if "boosting_duration_in_seconds" in value:
        out["boostingDurationInSeconds"] = value["boosting_duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> DateAttributeBoostingConfiguration:
    out: DateAttributeBoostingConfiguration = {}  # type: ignore[typeddict-item]
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
    if data.get("boostingDurationInSeconds") is not None:
        out["boosting_duration_in_seconds"] = data["boostingDurationInSeconds"]
    return out
