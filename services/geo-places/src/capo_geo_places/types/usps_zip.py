"""Generated from Smithy shape ``com.amazonaws.geoplaces#UspsZip``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.zip_classification_code


class UspsZip(TypedDict, closed=True):
    zip_classification_code: NotRequired[
        "capo_geo_places.types.zip_classification_code.ZipClassificationCode"
    ]
    """<p>The ZIP Classification Code, or in other words what type of postal code is it. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UspsZip) -> dict:
    out: dict = {}
    if "zip_classification_code" in value:
        import capo_geo_places.types.zip_classification_code

        out["ZipClassificationCode"] = (
            capo_geo_places.types.zip_classification_code.serialize_json(
                value["zip_classification_code"]
            )
        )
    return out


def deserialize_json(data: dict) -> UspsZip:
    out: UspsZip = {}  # type: ignore[typeddict-item]
    if data.get("ZipClassificationCode") is not None:
        import capo_geo_places.types.zip_classification_code

        out["zip_classification_code"] = (
            capo_geo_places.types.zip_classification_code.deserialize_json(
                data["ZipClassificationCode"]
            )
        )
    return out


def redact_sensitive(value: UspsZip) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "zip_classification_code" in value:
        out["zip_classification_code"] = "*** Sensitive Data Redacted ***"
    return out
