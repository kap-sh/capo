"""Generated from Smithy shape ``com.amazonaws.geoplaces#UspsZipPlus4``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.record_type_code


class UspsZipPlus4(TypedDict, closed=True):
    record_type_code: NotRequired[
        "capo_geo_places.types.record_type_code.RecordTypeCode"
    ]
    """<p>The USPS ZIP+4 Record Type Code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UspsZipPlus4) -> dict:
    out: dict = {}
    if "record_type_code" in value:
        import capo_geo_places.types.record_type_code

        out["RecordTypeCode"] = capo_geo_places.types.record_type_code.serialize_json(
            value["record_type_code"]
        )
    return out


def deserialize_json(data: dict) -> UspsZipPlus4:
    out: UspsZipPlus4 = {}  # type: ignore[typeddict-item]
    if data.get("RecordTypeCode") is not None:
        import capo_geo_places.types.record_type_code

        out["record_type_code"] = (
            capo_geo_places.types.record_type_code.deserialize_json(
                data["RecordTypeCode"]
            )
        )
    return out


def redact_sensitive(value: UspsZipPlus4) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "record_type_code" in value:
        out["record_type_code"] = "*** Sensitive Data Redacted ***"
    return out
