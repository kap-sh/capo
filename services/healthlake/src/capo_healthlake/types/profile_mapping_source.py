"""Generated from Smithy shape ``com.amazonaws.healthlake#ProfileMappingSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.string_map


class ProfileMappingSource(TypedDict, closed=True):
    profile_mapping: "capo_healthlake.types.string_map.StringMap"
    """<p>The content as a map of file paths to profile strings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProfileMappingSource) -> dict:
    out: dict = {}
    import capo_healthlake.types.string_map

    out["ProfileMapping"] = capo_healthlake.types.string_map.serialize_aws_json_1_0(
        value["profile_mapping"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ProfileMappingSource:
    out: ProfileMappingSource = {}  # type: ignore[typeddict-item]
    if data.get("ProfileMapping") is not None:
        import capo_healthlake.types.string_map

        out["profile_mapping"] = (
            capo_healthlake.types.string_map.deserialize_aws_json_1_0(
                data["ProfileMapping"]
            )
        )
    else:
        out["profile_mapping"] = {}
    return out
