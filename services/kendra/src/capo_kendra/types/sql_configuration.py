"""Generated from Smithy shape ``com.amazonaws.kendra#SqlConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.query_identifiers_enclosing_option


class SqlConfiguration(TypedDict, closed=True):
    query_identifiers_enclosing_option: NotRequired[
        "capo_kendra.types.query_identifiers_enclosing_option.QueryIdentifiersEnclosingOption"
    ]
    """<p>Determines whether Amazon Kendra encloses SQL identifiers for tables and column names in double quotes (") when making a database query.</p> <p>By default, Amazon Kendra passes SQL identifiers the way that they are entered into the data source configuration. It does not change the case of identifiers or enclose them in quotes.</p> <p>PostgreSQL internally converts uppercase characters to lower case characters in identifiers unless they are quoted. Choosing this option encloses identifiers in quotes so that PostgreSQL does not convert the character's case.</p> <p>For MySQL databases, you must enable the <code>ansi_quotes</code> option when you set this field to <code>DOUBLE_QUOTES</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqlConfiguration) -> dict:
    out: dict = {}
    if "query_identifiers_enclosing_option" in value:
        import capo_kendra.types.query_identifiers_enclosing_option

        out["QueryIdentifiersEnclosingOption"] = (
            capo_kendra.types.query_identifiers_enclosing_option.serialize_aws_json_1_1(
                value["query_identifiers_enclosing_option"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SqlConfiguration:
    out: SqlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("QueryIdentifiersEnclosingOption") is not None:
        import capo_kendra.types.query_identifiers_enclosing_option

        out["query_identifiers_enclosing_option"] = (
            capo_kendra.types.query_identifiers_enclosing_option.deserialize_aws_json_1_1(
                data["QueryIdentifiersEnclosingOption"]
            )
        )
    return out
