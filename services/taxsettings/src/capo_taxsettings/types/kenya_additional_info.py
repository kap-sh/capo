"""Generated from Smithy shape ``com.amazonaws.taxsettings#KenyaAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_taxsettings.types.person_type


class KenyaAdditionalInfo(TypedDict, closed=True):
    person_type: "capo_taxsettings.types.person_type.PersonType"
    """<p>The legal person or physical person assigned to this TRN in Kenya.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KenyaAdditionalInfo) -> dict:
    out: dict = {}
    import capo_taxsettings.types.person_type

    out["personType"] = capo_taxsettings.types.person_type.serialize_json(
        value["person_type"]
    )
    return out


def deserialize_json(data: dict) -> KenyaAdditionalInfo:
    out: KenyaAdditionalInfo = {}  # type: ignore[typeddict-item]
    if data.get("personType") is not None:
        import capo_taxsettings.types.person_type

        out["person_type"] = capo_taxsettings.types.person_type.deserialize_json(
            data["personType"]
        )
    else:
        import typing

        out["person_type"] = typing.cast(
            "capo_taxsettings.types.person_type.PersonType", ""
        )
    return out
