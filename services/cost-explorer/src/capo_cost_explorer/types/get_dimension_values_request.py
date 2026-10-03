"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetDimensionValuesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cost_explorer.types.billing_view_arn
    import capo_cost_explorer.types.context
    import capo_cost_explorer.types.date_interval
    import capo_cost_explorer.types.dimension
    import capo_cost_explorer.types.expression
    import capo_cost_explorer.types.max_results
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.search_string
    import capo_cost_explorer.types.sort_definitions


class GetDimensionValuesRequest(TypedDict, closed=True):
    search_string: NotRequired["capo_cost_explorer.types.search_string.SearchString"]
    """<p>The value that you want to search the filter values for.</p>"""
    time_period: "capo_cost_explorer.types.date_interval.DateInterval"
    """<p>The start date and end date for retrieving the dimension values. The start date is inclusive, but the end date is exclusive. For example, if <code>start</code> is <code>2017-01-01</code> and <code>end</code> is <code>2017-05-01</code>, then the cost and usage data is retrieved from <code>2017-01-01</code> up to and including <code>2017-04-30</code> but not including <code>2017-05-01</code>.</p>"""
    dimension: "capo_cost_explorer.types.dimension.Dimension"
    """<p>The name of the dimension. Each <code>Dimension</code> is available for a different <code>Context</code>. For more information, see <code>Context</code>. <code>LINK_ACCOUNT_NAME</code> and <code>SERVICE_CODE</code> can only be used in <a href="https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/AAPI_CostCategoryRule.html">CostCategoryRule</a>. </p>"""
    context: NotRequired["capo_cost_explorer.types.context.Context"]
    """<p>The context for the call to <code>GetDimensionValues</code>. This can be <code>RESERVATIONS</code> or <code>COST_AND_USAGE</code>. The default value is <code>COST_AND_USAGE</code>. If the context is set to <code>RESERVATIONS</code>, the resulting dimension values can be used in the <code>GetReservationUtilization</code> operation. If the context is set to <code>COST_AND_USAGE</code>, the resulting dimension values can be used in the <code>GetCostAndUsage</code> operation.</p> <p>If you set the context to <code>COST_AND_USAGE</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>AZ - The Availability Zone. An example is <code>us-east-1a</code>.</p> </li> <li> <p>BILLING_ENTITY - The Amazon Web Services seller that your account is with. Possible values are the following:</p> <p>- Amazon Web Services(Amazon Web Services): The entity that sells Amazon Web Services services.</p> <p>- AISPL (Amazon Internet Services Pvt. Ltd.): The local Indian entity that's an acting reseller for Amazon Web Services services in India.</p> <p>- Amazon Web Services Marketplace: The entity that supports the sale of solutions that are built on Amazon Web Services by third-party software providers.</p> </li> <li> <p>CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.</p> </li> <li> <p>DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are <code>SingleAZ</code> and <code>MultiAZ</code>.</p> </li> <li> <p>DATABASE_ENGINE - The Amazon Relational Database Service database. Examples are Aurora or MySQL.</p> </li> <li> <p>INSTANCE_TYPE - The type of Amazon EC2 instance. An example is <code>m4.xlarge</code>.</p> </li> <li> <p>INSTANCE_TYPE_FAMILY - A family of instance types optimized to fit different use cases. Examples are <code>Compute Optimized</code> (for example, <code>C4</code>, <code>C5</code>, <code>C6g</code>, and <code>C7g</code>), <code>Memory Optimization</code> (for example, <code>R4</code>, <code>R5n</code>, <code>R5b</code>, and <code>R6g</code>).</p> </li> <li> <p>INVOICING_ENTITY - The name of the entity that issues the Amazon Web Services invoice.</p> </li> <li> <p>LEGAL_ENTITY_NAME - The name of the organization that sells you Amazon Web Services services, such as Amazon Web Services.</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>OPERATING_SYSTEM - The operating system. Examples are Windows or Linux.</p> </li> <li> <p>OPERATION - The action performed. Examples include <code>RunInstance</code> and <code>CreateBucket</code>.</p> </li> <li> <p>PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.</p> </li> <li> <p>PURCHASE_TYPE - The reservation type of the purchase that this usage is related to. Examples include On-Demand Instances and Standard Reserved Instances.</p> </li> <li> <p>RESERVATION_ID - The unique identifier for an Amazon Web Services Reservation Instance.</p> </li> <li> <p>SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.</p> </li> <li> <p>SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute).</p> </li> <li> <p>SERVICE - The Amazon Web Services service such as Amazon DynamoDB.</p> </li> <li> <p>TENANCY - The tenancy of a resource. Examples are shared or dedicated.</p> </li> <li> <p>USAGE_TYPE - The type of usage. An example is DataTransfer-In-Bytes. The response for the <code>GetDimensionValues</code> operation includes a unit attribute. Examples include GB and Hrs.</p> </li> <li> <p>USAGE_TYPE_GROUP - The grouping of common usage types. An example is Amazon EC2: CloudWatch – Alarms. The response for this operation includes a unit attribute.</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>RECORD_TYPE - The different types of charges such as Reserved Instance (RI) fees, usage costs, tax refunds, and credits.</p> </li> <li> <p>RESOURCE_ID - The unique identifier of the resource. ResourceId is an opt-in feature only available for last 14 days for EC2-Compute Service.</p> </li> </ul> <p>If you set the context to <code>RESERVATIONS</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>AZ - The Availability Zone. An example is <code>us-east-1a</code>.</p> </li> <li> <p>CACHE_ENGINE - The Amazon ElastiCache operating system. Examples are Windows or Linux.</p> </li> <li> <p>DEPLOYMENT_OPTION - The scope of Amazon Relational Database Service deployments. Valid values are <code>SingleAZ</code> and <code>MultiAZ</code>.</p> </li> <li> <p>INSTANCE_TYPE - The type of Amazon EC2 instance. An example is <code>m4.xlarge</code>.</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>PLATFORM - The Amazon EC2 operating system. Examples are Windows or Linux.</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>SCOPE (Utilization only) - The scope of a Reserved Instance (RI). Values are regional or a single Availability Zone.</p> </li> <li> <p>TAG (Coverage only) - The tags that are associated with a Reserved Instance (RI).</p> </li> <li> <p>TENANCY - The tenancy of a resource. Examples are shared or dedicated.</p> </li> </ul> <p>If you set the context to <code>SAVINGS_PLANS</code>, you can use the following dimensions for searching:</p> <ul> <li> <p>SAVINGS_PLANS_TYPE - Type of Savings Plans (EC2 Instance or Compute)</p> </li> <li> <p>PAYMENT_OPTION - The payment option for the given Savings Plans (for example, All Upfront)</p> </li> <li> <p>REGION - The Amazon Web Services Region.</p> </li> <li> <p>INSTANCE_TYPE_FAMILY - The family of instances (For example, <code>m5</code>)</p> </li> <li> <p>LINKED_ACCOUNT - The description in the attribute map that includes the full name of the member account. The value field contains the Amazon Web Services ID of the member account.</p> </li> <li> <p>SAVINGS_PLAN_ARN - The unique identifier for your Savings Plans.</p> </li> </ul>"""
    filter: NotRequired["capo_cost_explorer.types.expression.Expression"]
    sort_by: NotRequired["capo_cost_explorer.types.sort_definitions.SortDefinitions"]
    """<p>The value that you want to sort the data by.</p> <p>The key represents cost and usage metrics. The following values are supported:</p> <ul> <li> <p> <code>BlendedCost</code> </p> </li> <li> <p> <code>UnblendedCost</code> </p> </li> <li> <p> <code>AmortizedCost</code> </p> </li> <li> <p> <code>NetAmortizedCost</code> </p> </li> <li> <p> <code>NetUnblendedCost</code> </p> </li> <li> <p> <code>UsageQuantity</code> </p> </li> <li> <p> <code>NormalizedUsageAmount</code> </p> </li> </ul> <p>The supported values for the <code>SortOrder</code> key are <code>ASCENDING</code> or <code>DESCENDING</code>.</p> <p>When you specify a <code>SortBy</code> paramater, the context must be <code>COST_AND_USAGE</code>. Further, when using <code>SortBy</code>, <code>NextPageToken</code> and <code>SearchString</code> aren't supported.</p>"""
    billing_view_arn: NotRequired[
        "capo_cost_explorer.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    max_results: NotRequired["capo_cost_explorer.types.max_results.MaxResults"]
    """<p>This field is only used when SortBy is provided in the request. The maximum number of objects that are returned for this request. If MaxResults isn't specified with SortBy, the request returns 1000 results as the default value for this parameter.</p> <p>For <code>GetDimensionValues</code>, MaxResults has an upper limit of 1000.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDimensionValuesRequest) -> dict:
    out: dict = {}
    if "search_string" in value:
        out["SearchString"] = value["search_string"]
    import capo_cost_explorer.types.date_interval

    out["TimePeriod"] = capo_cost_explorer.types.date_interval.serialize_aws_json_1_1(
        value["time_period"]
    )
    import capo_cost_explorer.types.dimension

    out["Dimension"] = capo_cost_explorer.types.dimension.serialize_aws_json_1_1(
        value["dimension"]
    )
    if "context" in value:
        import capo_cost_explorer.types.context

        out["Context"] = capo_cost_explorer.types.context.serialize_aws_json_1_1(
            value["context"]
        )
    if "filter" in value:
        import capo_cost_explorer.types.expression

        out["Filter"] = capo_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["filter"]
        )
    if "sort_by" in value:
        import capo_cost_explorer.types.sort_definitions

        out["SortBy"] = (
            capo_cost_explorer.types.sort_definitions.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDimensionValuesRequest:
    out: GetDimensionValuesRequest = {}  # type: ignore[typeddict-item]
    if data.get("SearchString") is not None:
        out["search_string"] = data["SearchString"]
    if data.get("TimePeriod") is not None:
        import capo_cost_explorer.types.date_interval

        out["time_period"] = (
            capo_cost_explorer.types.date_interval.deserialize_aws_json_1_1(
                data["TimePeriod"]
            )
        )
    else:
        raise DeserializationError("GetDimensionValuesRequest.time_period required")
    if data.get("Dimension") is not None:
        import capo_cost_explorer.types.dimension

        out["dimension"] = capo_cost_explorer.types.dimension.deserialize_aws_json_1_1(
            data["Dimension"]
        )
    else:
        raise DeserializationError("GetDimensionValuesRequest.dimension required")
    if data.get("Context") is not None:
        import capo_cost_explorer.types.context

        out["context"] = capo_cost_explorer.types.context.deserialize_aws_json_1_1(
            data["Context"]
        )
    if data.get("Filter") is not None:
        import capo_cost_explorer.types.expression

        out["filter"] = capo_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Filter"]
        )
    if data.get("SortBy") is not None:
        import capo_cost_explorer.types.sort_definitions

        out["sort_by"] = (
            capo_cost_explorer.types.sort_definitions.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("BillingViewArn") is not None:
        out["billing_view_arn"] = data["BillingViewArn"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    return out
