"""Generated from Smithy shape ``com.amazonaws.neptunedata#StartLoaderJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptunedata.errors import DeserializationError

if TYPE_CHECKING:
    import capo_neptunedata.types.format
    import capo_neptunedata.types.mode
    import capo_neptunedata.types.parallelism
    import capo_neptunedata.types.s3_bucket_region
    import capo_neptunedata.types.string_list
    import capo_neptunedata.types.string_valued_map


class StartLoaderJobInput(TypedDict, closed=True):
    source: "str"
    """<p>The <code>source</code> parameter accepts an S3 URI that identifies a single file, multiple files, a folder, or multiple folders. Neptune loads every data file in any folder that is specified.</p> <p>The URI can be in any of the following formats.</p> <ul> <li> <p> <code>s3://(bucket_name)/(object-key-name)</code> </p> </li> <li> <p> <code>https://s3.amazonaws.com/(bucket_name)/(object-key-name)</code> </p> </li> <li> <p> <code>https://s3.us-east-1.amazonaws.com/(bucket_name)/(object-key-name)</code> </p> </li> </ul> <p>The <code>object-key-name</code> element of the URI is equivalent to the <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html#API_ListObjects_RequestParameters">prefix</a> parameter in an S3 <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html">ListObjects</a> API call. It identifies all the objects in the specified S3 bucket whose names begin with that prefix. That can be a single file or folder, or multiple files and/or folders.</p> <p>The specified folder or folders can contain multiple vertex files and multiple edge files.</p>"""
    format: "capo_neptunedata.types.format.Format"
    r"""<p>The format of the data. For more information about data formats for the Neptune <code>Loader</code> command, see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format.html">Load Data Formats</a>.</p> <p class="title"> <b>Allowed values</b> </p> <ul> <li> <p> <b> <code>csv</code> </b> for the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-gremlin.html">Gremlin CSV data format</a>.</p> </li> <li> <p> <b> <code>opencypher</code> </b> for the <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-format-opencypher.html">openCypher CSV data format</a>.</p> </li> <li> <p> <b> <code>ntriples</code> </b> for the <a href="https://www.w3.org/TR/n-triples/">N-Triples RDF data format</a>.</p> </li> <li> <p> <b> <code>nquads</code> </b> for the <a href="https://www.w3.org/TR/n-quads/">N-Quads RDF data format</a>.</p> </li> <li> <p> <b> <code>rdfxml</code> </b> for the <a href="https://www.w3.org/TR/rdf-syntax-grammar/">RDF\XML RDF data format</a>.</p> </li> <li> <p> <b> <code>turtle</code> </b> for the <a href="https://www.w3.org/TR/turtle/">Turtle RDF data format</a>.</p> </li> </ul>"""
    s3_bucket_region: "capo_neptunedata.types.s3_bucket_region.S3BucketRegion"
    """<p>The Amazon region of the S3 bucket. This must match the Amazon Region of the DB cluster.</p>"""
    iam_role_arn: "str"
    """<p>The Amazon Resource Name (ARN) for an IAM role to be assumed by the Neptune DB instance for access to the S3 bucket. The IAM role ARN provided here should be attached to the DB cluster (see <a href="https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM-add-role-cluster.html">Adding the IAM Role to an Amazon Neptune Cluster</a>.</p>"""
    mode: NotRequired["capo_neptunedata.types.mode.Mode"]
    """<p>The load job mode.</p> <p> <i>Allowed values</i>: <code>RESUME</code>, <code>NEW</code>, <code>AUTO</code>.</p> <p> <i>Default value</i>: <code>AUTO</code>.</p> <p class="title"> <b/> </p> <ul> <li> <p> <code>RESUME</code> - In RESUME mode, the loader looks for a previous load from this source, and if it finds one, resumes that load job. If no previous load job is found, the loader stops.</p> <p>The loader avoids reloading files that were successfully loaded in a previous job. It only tries to process failed files. If you dropped previously loaded data from your Neptune cluster, that data is not reloaded in this mode. If a previous load job loaded all files from the same source successfully, nothing is reloaded, and the loader returns success.</p> </li> <li> <p> <code>NEW</code> - In NEW mode, the creates a new load request regardless of any previous loads. You can use this mode to reload all the data from a source after dropping previously loaded data from your Neptune cluster, or to load new data available at the same source.</p> </li> <li> <p> <code>AUTO</code> - In AUTO mode, the loader looks for a previous load job from the same source, and if it finds one, resumes that job, just as in <code>RESUME</code> mode.</p> <p>If the loader doesn't find a previous load job from the same source, it loads all data from the source, just as in <code>NEW</code> mode.</p> </li> </ul>"""
    fail_on_error: NotRequired["bool"]
    """<p> <b> <code>failOnError</code> </b> - A flag to toggle a complete stop on an error.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"TRUE"</code>.</p> <p>When this parameter is set to <code>"FALSE"</code>, the loader tries to load all the data in the location specified, skipping any entries with errors.</p> <p>When this parameter is set to <code>"TRUE"</code>, the loader stops as soon as it encounters an error. Data loaded up to that point persists.</p>"""
    parallelism: NotRequired["capo_neptunedata.types.parallelism.Parallelism"]
    """<p>The optional <code>parallelism</code> parameter can be set to reduce the number of threads used by the bulk load process.</p> <p> <i>Allowed values</i>:</p> <ul> <li> <p> <code>LOW</code> – The number of threads used is the number of available vCPUs divided by 8.</p> </li> <li> <p> <code>MEDIUM</code> – The number of threads used is the number of available vCPUs divided by 2.</p> </li> <li> <p> <code>HIGH</code> – The number of threads used is the same as the number of available vCPUs.</p> </li> <li> <p> <code>OVERSUBSCRIBE</code> – The number of threads used is the number of available vCPUs multiplied by 2. If this value is used, the bulk loader takes up all available resources.</p> <p>This does not mean, however, that the <code>OVERSUBSCRIBE</code> setting results in 100% CPU utilization. Because the load operation is I/O bound, the highest CPU utilization to expect is in the 60% to 70% range.</p> </li> </ul> <p> <i>Default value</i>: <code>HIGH</code> </p> <p>The <code>parallelism</code> setting can sometimes result in a deadlock between threads when loading openCypher data. When this happens, Neptune returns the <code>LOAD_DATA_DEADLOCK</code> error. You can generally fix the issue by setting <code>parallelism</code> to a lower setting and retrying the load command.</p>"""
    parser_configuration: NotRequired[
        "capo_neptunedata.types.string_valued_map.StringValuedMap"
    ]
    """<p> <b> <code>parserConfiguration</code> </b> – An optional object with additional parser configuration values. Each of the child parameters is also optional:</p> <p class="title"> <b/> </p> <ul> <li> <p> <b> <code>namedGraphUri</code> </b> - The default graph for all RDF formats when no graph is specified (for non-quads formats and NQUAD entries with no graph).</p> <p>The default is <code>https://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph</code>.</p> </li> <li> <p> <b> <code>baseUri</code> </b> - The base URI for RDF/XML and Turtle formats.</p> <p>The default is <code>https://aws.amazon.com/neptune/default</code>.</p> </li> <li> <p> <b> <code>allowEmptyStrings</code> </b> - Gremlin users need to be able to pass empty string values("") as node and edge properties when loading CSV data. If <code>allowEmptyStrings</code> is set to <code>false</code> (the default), such empty strings are treated as nulls and are not loaded.</p> <p>If <code>allowEmptyStrings</code> is set to <code>true</code>, the loader treats empty strings as valid property values and loads them accordingly.</p> </li> </ul>"""
    update_single_cardinality_properties: NotRequired["bool"]
    """<p> <code>updateSingleCardinalityProperties</code> is an optional parameter that controls how the bulk loader treats a new value for single-cardinality vertex or edge properties. This is not supported for loading openCypher data.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p> <p>By default, or when <code>updateSingleCardinalityProperties</code> is explicitly set to <code>"FALSE"</code>, the loader treats a new value as an error, because it violates single cardinality.</p> <p>When <code>updateSingleCardinalityProperties</code> is set to <code>"TRUE"</code>, on the other hand, the bulk loader replaces the existing value with the new one. If multiple edge or single-cardinality vertex property values are provided in the source file(s) being loaded, the final value at the end of the bulk load could be any one of those new values. The loader only guarantees that the existing value has been replaced by one of the new ones.</p>"""
    queue_request: NotRequired["bool"]
    """<p>This is an optional flag parameter that indicates whether the load request can be queued up or not. </p> <p>You don't have to wait for one load job to complete before issuing the next one, because Neptune can queue up as many as 64 jobs at a time, provided that their <code>queueRequest</code> parameters are all set to <code>"TRUE"</code>. The queue order of the jobs will be first-in-first-out (FIFO).</p> <p>If the <code>queueRequest</code> parameter is omitted or set to <code>"FALSE"</code>, the load request will fail if another load job is already running.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p>"""
    dependencies: NotRequired["capo_neptunedata.types.string_list.StringList"]
    """<p>This is an optional parameter that can make a queued load request contingent on the successful completion of one or more previous jobs in the queue.</p> <p>Neptune can queue up as many as 64 load requests at a time, if their <code>queueRequest</code> parameters are set to <code>"TRUE"</code>. The <code>dependencies</code> parameter lets you make execution of such a queued request dependent on the successful completion of one or more specified previous requests in the queue.</p> <p>For example, if load <code>Job-A</code> and <code>Job-B</code> are independent of each other, but load <code>Job-C</code> needs <code>Job-A</code> and <code>Job-B</code> to be finished before it begins, proceed as follows:</p> <ol> <li> <p>Submit <code>load-job-A</code> and <code>load-job-B</code> one after another in any order, and save their load-ids.</p> </li> <li> <p>Submit <code>load-job-C</code> with the load-ids of the two jobs in its <code>dependencies</code> field:</p> </li> </ol> <p>Because of the <code>dependencies</code> parameter, the bulk loader will not start <code>Job-C</code> until <code>Job-A</code> and <code>Job-B</code> have completed successfully. If either one of them fails, Job-C will not be executed, and its status will be set to <code>LOAD_FAILED_BECAUSE_DEPENDENCY_NOT_SATISFIED</code>.</p> <p>You can set up multiple levels of dependency in this way, so that the failure of one job will cause all requests that are directly or indirectly dependent on it to be cancelled.</p>"""
    user_provided_edge_ids: NotRequired["bool"]
    """<p>This parameter is required only when loading openCypher data that contains relationship IDs. It must be included and set to <code>True</code> when openCypher relationship IDs are explicitly provided in the load data (recommended).</p> <p>When <code>userProvidedEdgeIds</code> is absent or set to <code>True</code>, an <code>:ID</code> column must be present in every relationship file in the load.</p> <p>When <code>userProvidedEdgeIds</code> is present and set to <code>False</code>, relationship files in the load <b>must not</b> contain an <code>:ID</code> column. Instead, the Neptune loader automatically generates an ID for each relationship.</p> <p>It's useful to provide relationship IDs explicitly so that the loader can resume loading after error in the CSV data have been fixed, without having to reload any relationships that have already been loaded. If relationship IDs have not been explicitly assigned, the loader cannot resume a failed load if any relationship file has had to be corrected, and must instead reload all the relationships.</p>"""
    edge_only_load: NotRequired["bool"]
    """<p> <b> <code>edgeOnlyLoad</code> </b> - A flag that controls file processing order during bulk loading.</p> <p> <i>Allowed values</i>: <code>"TRUE"</code>, <code>"FALSE"</code>.</p> <p> <i>Default value</i>: <code>"FALSE"</code>.</p> <p>When this parameter is set to "FALSE", the loader automatically loads vertex files first, then edge files afterwards. It does this by first scanning all files to determine their contents (vertices or edges). When this parameter is set to "TRUE", the loader skips the initial scanning phase and immediately loads all files in the order they appear.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartLoaderJobInput) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    import capo_neptunedata.types.format

    out["format"] = capo_neptunedata.types.format.serialize_json(value["format"])
    import capo_neptunedata.types.s3_bucket_region

    out["region"] = capo_neptunedata.types.s3_bucket_region.serialize_json(
        value["s3_bucket_region"]
    )
    out["iamRoleArn"] = value["iam_role_arn"]
    if "mode" in value:
        import capo_neptunedata.types.mode

        out["mode"] = capo_neptunedata.types.mode.serialize_json(value["mode"])
    if "fail_on_error" in value:
        out["failOnError"] = value["fail_on_error"]
    if "parallelism" in value:
        import capo_neptunedata.types.parallelism

        out["parallelism"] = capo_neptunedata.types.parallelism.serialize_json(
            value["parallelism"]
        )
    if "parser_configuration" in value:
        import capo_neptunedata.types.string_valued_map

        out["parserConfiguration"] = (
            capo_neptunedata.types.string_valued_map.serialize_json(
                value["parser_configuration"]
            )
        )
    if "update_single_cardinality_properties" in value:
        out["updateSingleCardinalityProperties"] = value[
            "update_single_cardinality_properties"
        ]
    if "queue_request" in value:
        out["queueRequest"] = value["queue_request"]
    if "dependencies" in value:
        import capo_neptunedata.types.string_list

        out["dependencies"] = capo_neptunedata.types.string_list.serialize_json(
            value["dependencies"]
        )
    if "user_provided_edge_ids" in value:
        out["userProvidedEdgeIds"] = value["user_provided_edge_ids"]
    if "edge_only_load" in value:
        out["edgeOnlyLoad"] = value["edge_only_load"]
    return out


def deserialize_json(data: dict) -> StartLoaderJobInput:
    out: StartLoaderJobInput = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        out["source"] = data["source"]
    else:
        raise DeserializationError("StartLoaderJobInput.source required")
    if data.get("format") is not None:
        import capo_neptunedata.types.format

        out["format"] = capo_neptunedata.types.format.deserialize_json(data["format"])
    else:
        raise DeserializationError("StartLoaderJobInput.format required")
    if data.get("region") is not None:
        import capo_neptunedata.types.s3_bucket_region

        out["s3_bucket_region"] = (
            capo_neptunedata.types.s3_bucket_region.deserialize_json(data["region"])
        )
    else:
        raise DeserializationError("StartLoaderJobInput.s3_bucket_region required")
    if data.get("iamRoleArn") is not None:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        raise DeserializationError("StartLoaderJobInput.iam_role_arn required")
    if data.get("mode") is not None:
        import capo_neptunedata.types.mode

        out["mode"] = capo_neptunedata.types.mode.deserialize_json(data["mode"])
    if data.get("failOnError") is not None:
        out["fail_on_error"] = data["failOnError"]
    if data.get("parallelism") is not None:
        import capo_neptunedata.types.parallelism

        out["parallelism"] = capo_neptunedata.types.parallelism.deserialize_json(
            data["parallelism"]
        )
    if data.get("parserConfiguration") is not None:
        import capo_neptunedata.types.string_valued_map

        out["parser_configuration"] = (
            capo_neptunedata.types.string_valued_map.deserialize_json(
                data["parserConfiguration"]
            )
        )
    if data.get("updateSingleCardinalityProperties") is not None:
        out["update_single_cardinality_properties"] = data[
            "updateSingleCardinalityProperties"
        ]
    if data.get("queueRequest") is not None:
        out["queue_request"] = data["queueRequest"]
    if data.get("dependencies") is not None:
        import capo_neptunedata.types.string_list

        out["dependencies"] = capo_neptunedata.types.string_list.deserialize_json(
            data["dependencies"]
        )
    if data.get("userProvidedEdgeIds") is not None:
        out["user_provided_edge_ids"] = data["userProvidedEdgeIds"]
    if data.get("edgeOnlyLoad") is not None:
        out["edge_only_load"] = data["edgeOnlyLoad"]
    return out
