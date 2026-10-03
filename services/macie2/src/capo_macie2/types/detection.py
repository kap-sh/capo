"""Generated from Smithy shape ``com.amazonaws.macie2#Detection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean
    import capo_macie2.types.__long
    import capo_macie2.types.__string
    import capo_macie2.types.data_identifier_type


class Detection(TypedDict, closed=True):
    arn: NotRequired["capo_macie2.types.__string.__string"]
    """<p>If the sensitive data was detected by a custom data identifier, the Amazon Resource Name (ARN) of the custom data identifier that detected the data. Otherwise, this value is null.</p>"""
    count: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The total number of occurrences of the sensitive data.</p>"""
    id: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The unique identifier for the custom data identifier or managed data identifier that detected the sensitive data. For additional details about a specified managed data identifier, see <a href="https://docs.aws.amazon.com/macie/latest/user/managed-data-identifiers.html">Using managed data identifiers</a> in the <i>Amazon Macie User Guide</i>.</p>"""
    name: NotRequired["capo_macie2.types.__string.__string"]
    """<p>The name of the custom data identifier or managed data identifier that detected the sensitive data. For a managed data identifier, this value is the same as the unique identifier (id).</p>"""
    suppressed: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether occurrences of this type of sensitive data are excluded (true) or included (false) in the bucket's sensitivity score, if the score is calculated by Amazon Macie.</p>"""
    type: NotRequired["capo_macie2.types.data_identifier_type.DataIdentifierType"]
    """<p>The type of data identifier that detected the sensitive data. Possible values are: CUSTOM, for a custom data identifier; and, MANAGED, for a managed data identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Detection) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "count" in value:
        out["count"] = value["count"]
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "suppressed" in value:
        out["suppressed"] = value["suppressed"]
    if "type" in value:
        import capo_macie2.types.data_identifier_type

        out["type"] = capo_macie2.types.data_identifier_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> Detection:
    out: Detection = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("count") is not None:
        out["count"] = data["count"]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("suppressed") is not None:
        out["suppressed"] = data["suppressed"]
    if data.get("type") is not None:
        import capo_macie2.types.data_identifier_type

        out["type"] = capo_macie2.types.data_identifier_type.deserialize_json(
            data["type"]
        )
    return out
