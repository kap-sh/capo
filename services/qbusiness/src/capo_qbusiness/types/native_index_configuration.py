"""Generated from Smithy shape ``com.amazonaws.qbusiness#NativeIndexConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.document_attribute_boosting_override_map
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.long


class NativeIndexConfiguration(TypedDict, closed=True):
    index_id: "capo_qbusiness.types.index_id.IndexId"
    """<p>The identifier for the Amazon Q Business index.</p>"""
    version: NotRequired["capo_qbusiness.types.long.Long"]
    """<p>A read-only field that specifies the version of the <code>NativeIndexConfiguration</code>.</p> <p>Amazon Q Business introduces enhanced document retrieval capabilities in version 2 of <code>NativeIndexConfiguration</code>, focusing on streamlined metadata boosting that prioritizes recency and source relevance to deliver more accurate responses to your queries. Version 2 has the following differences from version 1:</p> <ul> <li> <p>Version 2 supports a single Date field (created_at OR last_updated_at) for recency boosting</p> </li> <li> <p>Version 2 supports a single String field with an ordered list of up to 5 values</p> </li> <li> <p>Version 2 introduces number-based boost levels (ONE, TWO) alongside the text-based levels</p> </li> <li> <p>Version 2 allows specifying prioritization between Date and String fields</p> </li> <li> <p>Version 2 maintains backward compatibility with existing configurations</p> </li> </ul>"""
    boosting_override: NotRequired[
        "capo_qbusiness.types.document_attribute_boosting_override_map.DocumentAttributeBoostingOverrideMap"
    ]
    """<p>Overrides the default boosts applied by Amazon Q Business to supported document attribute data types.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NativeIndexConfiguration) -> dict:
    out: dict = {}
    out["indexId"] = value["index_id"]
    if "version" in value:
        out["version"] = value["version"]
    if "boosting_override" in value:
        import capo_qbusiness.types.document_attribute_boosting_override_map

        out["boostingOverride"] = (
            capo_qbusiness.types.document_attribute_boosting_override_map.serialize_json(
                value["boosting_override"]
            )
        )
    return out


def deserialize_json(data: dict) -> NativeIndexConfiguration:
    out: NativeIndexConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("indexId") is not None:
        out["index_id"] = data["indexId"]
    else:
        out["index_id"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("boostingOverride") is not None:
        import capo_qbusiness.types.document_attribute_boosting_override_map

        out["boosting_override"] = (
            capo_qbusiness.types.document_attribute_boosting_override_map.deserialize_json(
                data["boostingOverride"]
            )
        )
    return out
