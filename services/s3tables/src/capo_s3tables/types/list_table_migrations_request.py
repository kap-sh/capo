"""Generated from Smithy shape ``com.amazonaws.s3tables#ListTableMigrationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.list_table_migrations_limit
    import capo_s3tables.types.migration_state
    import capo_s3tables.types.namespace_name
    import capo_s3tables.types.next_token
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_name


class ListTableMigrationsRequest(TypedDict, closed=True):
    table_bucket_arn: NotRequired["capo_s3tables.types.table_bucket_arn.TableBucketARN"]
    """<p>The Amazon Resource Name (ARN) of the table bucket to list migrations for.</p>"""
    namespace: NotRequired["capo_s3tables.types.namespace_name.NamespaceName"]
    """<p>The namespace to list migrations for. Requires <code>tableBucketARN</code>.</p>"""
    name: NotRequired["capo_s3tables.types.table_name.TableName"]
    """<p>The name of the table to list migrations for. Requires <code>tableBucketARN</code> and <code>namespace</code>.</p>"""
    table_arn: NotRequired["capo_s3tables.types.table_arn.TableARN"]
    """<p>The Amazon Resource Name (ARN) of the table to list migrations for. The list includes the migrations into this table. To also list migrations into an earlier table of the same name, specify <code>tableBucketARN</code>, <code>namespace</code> and <code>name</code> instead. Specify either <code>tableARN</code> or <code>tableBucketARN</code>, not both.</p>"""
    state: NotRequired["capo_s3tables.types.migration_state.MigrationState"]
    """<p>The state to filter the list by. For the valid values, see the <code>state</code> member of <code>GetTableMigration</code>.</p>"""
    has_valid_plan: NotRequired["bool"]
    """<p>The <code>hasValidPlan</code> value to filter the list by. Migrations that are still planning aren't listed, whichever value you specify.</p>"""
    max_results: NotRequired[
        "capo_s3tables.types.list_table_migrations_limit.ListTableMigrationsLimit"
    ]
    """<p>The maximum number of migrations to return, from 1 to 1,000. If you don't specify a value, the default is 100.</p>"""
    next_token: NotRequired["capo_s3tables.types.next_token.NextToken"]
    """<p>The <code>nextToken</code> from a previous response, to get the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTableMigrationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTableMigrationsRequest:
    out: ListTableMigrationsRequest = {}  # type: ignore[typeddict-item]
    return out
