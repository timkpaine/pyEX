# *****************************************************************************
#
# Copyright (c) 2021, the pyEX authors.
#
# This file is part of the pyEX library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#
from functools import wraps

import pandas as pd

from ..common import _get


def isinLookup(isin, token="", version="stable", filter="", format="json"):
    """This call converts an ISIN to an iex symbol

    https://iexcloud.io/docs/api/#isin-mapping
    8am, 9am, 12pm, 1pm UTC daily

    Args:
        isin (str): isin to lookup
        token (str): Access token
        version (str): API version
        filter (str): filters: https://iexcloud.io/docs/api/#filter-results
        format (str): return format, defaults to json

    Returns:
        dict or DataFrame or list: result
    """
    return _get(
        "ref-data/isin?isin={}".format(isin),
        token=token,
        version=version,
        filter=filter,
        format=format,
    )


@wraps(isinLookup)
def isinLookupDF(*args, **kwargs):
    return pd.DataFrame(isinLookup(*args, **kwargs))
