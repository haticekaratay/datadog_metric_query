"""
Aggregate spans returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spans_api import SpansApi
from datadog_api_client.v2.model.spans_aggregate_data import SpansAggregateData
from datadog_api_client.v2.model.spans_aggregate_request import SpansAggregateRequest
from datadog_api_client.v2.model.spans_aggregate_request_attributes import SpansAggregateRequestAttributes
from datadog_api_client.v2.model.spans_aggregate_request_type import SpansAggregateRequestType
from datadog_api_client.v2.model.spans_aggregation_function import SpansAggregationFunction
from datadog_api_client.v2.model.spans_compute import SpansCompute
from datadog_api_client.v2.model.spans_compute_type import SpansComputeType
from datadog_api_client.v2.model.spans_query_filter import SpansQueryFilter
from datadog_api_client.v2.model.spans_list_request import SpansListRequest
from datetime import datetime, timedelta, timezone
from datadog_api_client.v2.model.spans_list_request_data import SpansListRequestData
from datadog_api_client.v2.model.spans_list_request_page import SpansListRequestPage
from datadog_api_client.v2.model.spans_list_request_attributes import SpansListRequestAttributes
import os

# cfg = Configuration(server_variables={"site": "us1"})
cfg = Configuration()
now = datetime.now(timezone.utc)
start_time = now-timedelta(minutes=5)

_from = start_time.isoformat().replace("+00:00", "Z")
_to = now.isoformat().replace("+00:00", "Z")

body = SpansListRequest(
    data=SpansListRequestData(
        attributes=SpansListRequestAttributes(
            filter=SpansQueryFilter(
                _from=_from,
                to=_to,
                query="service:imviz"
            ),
            page=SpansListRequestPage(limit=5),
            sort="timestamp",
        ),
        type="search_request",
    )
)

with ApiClient(cfg) as client:
    api = SpansApi(client)
    res = api.list_spans(body)

print("spans found:", len(res.data))
print(res.to_dict())
