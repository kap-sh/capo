"""Generated from Smithy shape ``com.amazonaws.taxsettings#SpainAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.registration_type


class SpainAdditionalInfo(TypedDict, closed=True):
    registration_type: "capo_taxsettings.types.registration_type.RegistrationType"
    """<p>The registration type in Spain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpainAdditionalInfo) -> dict:
    out: dict = {}
    import capo_taxsettings.types.registration_type

    out["registrationType"] = capo_taxsettings.types.registration_type.serialize_json(
        value["registration_type"]
    )
    return out


def deserialize_json(data: dict) -> SpainAdditionalInfo:
    out: SpainAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("registrationType") is not None:
        import capo_taxsettings.types.registration_type

        out["registration_type"] = (
            capo_taxsettings.types.registration_type.deserialize_json(
                data["registrationType"]
            )
        )
    else:
        import typing

        out["registration_type"] = typing.cast(
            "capo_taxsettings.types.registration_type.RegistrationType", ""
        )
    return out
