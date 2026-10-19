"""Generated from Smithy shape ``com.amazonaws.oam#MetricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_oam.types.metrics_filter


class MetricConfiguration(TypedDict, closed=True):
    filter: "capo_oam.types.metrics_filter.MetricsFilter"
    """<p>Use this field to specify which metrics are to be shared with the monitoring account. Use the term <code>Namespace</code> and one or more of the following operands. Use single quotation marks (') around namespace names. The matching of namespace names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are <code>AND</code> and <code>OR</code>.</p> <ul> <li> <p> <code>=</code> and <code>!=</code> </p> </li> <li> <p> <code>AND</code> </p> </li> <li> <p> <code>OR</code> </p> </li> <li> <p> <code>LIKE</code> and <code>NOT LIKE</code>. These can be used only as prefix searches. Include a <code>%</code> at the end of the string that you want to search for and include.</p> </li> <li> <p> <code>IN</code> and <code>NOT IN</code>, using parentheses <code>( )</code> </p> </li> </ul> <p>Examples:</p> <ul> <li> <p> <code>Namespace NOT LIKE 'AWS/%'</code> includes only namespaces that don't start with <code>AWS/</code>, such as custom namespaces.</p> </li> <li> <p> <code>Namespace IN ('AWS/EC2', 'AWS/ELB', 'AWS/S3')</code> includes only the metrics in the EC2, Elastic Load Balancing, and Amazon S3 namespaces. </p> </li> <li> <p> <code>Namespace = 'AWS/EC2' OR Namespace NOT LIKE 'AWS/%'</code> includes only the EC2 namespace and your custom namespaces.</p> </li> </ul> <note> <p>If you are updating a link that uses filters, you can specify <code>*</code> as the only value for the <code>filter</code> parameter to delete the filter and share all metric namespaces with the monitoring account.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricConfiguration) -> dict:
    out: dict = {}
    out["Filter"] = value["filter"]
    return out


def deserialize_json(data: dict) -> MetricConfiguration:
    out: MetricConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("Filter") is not None:
        out["filter"] = data["Filter"]
    else:
        out["filter"] = ""
    return out
