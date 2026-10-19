"""Generated from Smithy shape ``com.amazonaws.chimesdkidentity#ExpirationSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_identity.types.expiration_criterion
    import capo_chime_sdk_identity.types.expiration_days


class ExpirationSettings(TypedDict, closed=True):
    expiration_days: "capo_chime_sdk_identity.types.expiration_days.ExpirationDays"
    """<p>The period in days after which an <code>AppInstanceUser</code> will be automatically deleted.</p>"""
    expiration_criterion: (
        "capo_chime_sdk_identity.types.expiration_criterion.ExpirationCriterion"
    )
    """<p>Specifies the conditions under which an <code>AppInstanceUser</code> will expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpirationSettings) -> dict:
    out: dict = {}
    out["ExpirationDays"] = value["expiration_days"]
    import capo_chime_sdk_identity.types.expiration_criterion

    out["ExpirationCriterion"] = (
        capo_chime_sdk_identity.types.expiration_criterion.serialize_json(
            value["expiration_criterion"]
        )
    )
    return out


def deserialize_json(data: dict) -> ExpirationSettings:
    out: ExpirationSettings = {}  # type: ignore[typeddict-item]
    if data.get("ExpirationDays") is not None:
        out["expiration_days"] = data["ExpirationDays"]
    else:
        out["expiration_days"] = 0
    if data.get("ExpirationCriterion") is not None:
        import capo_chime_sdk_identity.types.expiration_criterion

        out["expiration_criterion"] = (
            capo_chime_sdk_identity.types.expiration_criterion.deserialize_json(
                data["ExpirationCriterion"]
            )
        )
    else:
        import typing

        out["expiration_criterion"] = typing.cast(
            "capo_chime_sdk_identity.types.expiration_criterion.ExpirationCriterion", ""
        )
    return out
