"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Attribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.default_value


class Attribute(TypedDict, closed=True):
    default_value: NotRequired["capo_iotsitewise.types.default_value.DefaultValue"]
    """<p>The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attribute's value after you create an asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html">Updating attribute values</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attribute) -> dict:
    out: dict = {}
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    return out


def deserialize_json(data: dict) -> Attribute:
    out: Attribute = {}  # type: ignore[typeddict-item]
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    return out
