"""Generated from Smithy shape ``com.amazonaws.s3tables#MigrationPolicies``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.incompatible_values_policy
    import capo_s3tables.types.unmatched_source_fields_policy


class MigrationPolicies(TypedDict, closed=True):
    unmatched_source_fields_policy: (
        "capo_s3tables.types.unmatched_source_fields_policy.UnmatchedSourceFieldsPolicy"
    )
    """<p>The migration policy for a source field that has no matching column in the destination schema. Valid values:</p> <ul> <li> <p> <code>fail</code> - Fails the migration. This is the default.</p> </li> <li> <p> <code>drop</code> - Leaves source columns that the destination schema doesn't have out of the destination table, and doesn't migrate source objects outside the Amazon Web Services Glue table's partition locations.</p> </li> </ul> <p>A destination schema that leaves out a partition column or a field of a struct column fails the migration under either value.</p>"""
    incompatible_values_policy: (
        "capo_s3tables.types.incompatible_values_policy.IncompatibleValuesPolicy"
    )
    """<p>The migration policy for a source value that the destination column's type can't hold. Valid values:</p> <ul> <li> <p> <code>fail</code> - Fails the migration. This is the default.</p> </li> <li> <p> <code>setNull</code> - Writes null for a value that the destination column's type can't hold. If a column's type in a source object is incompatible with the destination column's type, the column is null for that whole object.</p> </li> </ul> <p>A required column, or a type that migration doesn't support, fails the migration under either value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MigrationPolicies) -> dict:
    out: dict = {}
    import capo_s3tables.types.unmatched_source_fields_policy

    out["unmatchedSourceFieldsPolicy"] = (
        capo_s3tables.types.unmatched_source_fields_policy.serialize_json(
            value.get("unmatched_source_fields_policy", "fail")
        )
    )
    import capo_s3tables.types.incompatible_values_policy

    out["incompatibleValuesPolicy"] = (
        capo_s3tables.types.incompatible_values_policy.serialize_json(
            value.get("incompatible_values_policy", "fail")
        )
    )
    return out


def deserialize_json(data: dict) -> MigrationPolicies:
    out: MigrationPolicies = {}  # type: ignore[typeddict-item]
    if data.get("unmatchedSourceFieldsPolicy") is not None:
        import capo_s3tables.types.unmatched_source_fields_policy

        out["unmatched_source_fields_policy"] = (
            capo_s3tables.types.unmatched_source_fields_policy.deserialize_json(
                data["unmatchedSourceFieldsPolicy"]
            )
        )
    else:
        out["unmatched_source_fields_policy"] = "fail"
    if data.get("incompatibleValuesPolicy") is not None:
        import capo_s3tables.types.incompatible_values_policy

        out["incompatible_values_policy"] = (
            capo_s3tables.types.incompatible_values_policy.deserialize_json(
                data["incompatibleValuesPolicy"]
            )
        )
    else:
        out["incompatible_values_policy"] = "fail"
    return out
