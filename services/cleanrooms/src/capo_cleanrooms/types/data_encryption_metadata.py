"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DataEncryptionMetadata``."""

from typing_extensions import TypedDict


class DataEncryptionMetadata(TypedDict, closed=True):
    allow_cleartext: "bool"
    """<p>Indicates whether encrypted tables can contain cleartext data (<code>TRUE</code>) or are to cryptographically process every column (<code>FALSE</code>).</p>"""
    allow_duplicates: "bool"
    """<p>Indicates whether Fingerprint columns can contain duplicate entries (<code>TRUE</code>) or are to contain only non-repeated values (<code>FALSE</code>).</p>"""
    allow_joins_on_columns_with_different_names: "bool"
    """<p>Indicates whether Fingerprint columns can be joined on any other Fingerprint column with a different name (<code>TRUE</code>) or can only be joined on Fingerprint columns of the same name (<code>FALSE</code>).</p>"""
    preserve_nulls: "bool"
    """<p>Indicates whether NULL values are to be copied as NULL to encrypted tables (<code>TRUE</code>) or cryptographically processed (<code>FALSE</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataEncryptionMetadata) -> dict:
    out: dict = {}
    out["allowCleartext"] = value["allow_cleartext"]
    out["allowDuplicates"] = value["allow_duplicates"]
    out["allowJoinsOnColumnsWithDifferentNames"] = value[
        "allow_joins_on_columns_with_different_names"
    ]
    out["preserveNulls"] = value["preserve_nulls"]
    return out


def deserialize_json(data: dict) -> DataEncryptionMetadata:
    out: DataEncryptionMetadata = {}  # type: ignore[typeddict-item]
    if data.get("allowCleartext") is not None:
        out["allow_cleartext"] = data["allowCleartext"]
    else:
        out["allow_cleartext"] = False
    if data.get("allowDuplicates") is not None:
        out["allow_duplicates"] = data["allowDuplicates"]
    else:
        out["allow_duplicates"] = False
    if data.get("allowJoinsOnColumnsWithDifferentNames") is not None:
        out["allow_joins_on_columns_with_different_names"] = data[
            "allowJoinsOnColumnsWithDifferentNames"
        ]
    else:
        out["allow_joins_on_columns_with_different_names"] = False
    if data.get("preserveNulls") is not None:
        out["preserve_nulls"] = data["preserveNulls"]
    else:
        out["preserve_nulls"] = False
    return out
