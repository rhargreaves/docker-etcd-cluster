#!/usr/bin/env python3
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning, module="google.protobuf")
warnings.filterwarnings("ignore", category=DeprecationWarning, module="etcd3")

import etcd3


def test_etcd():
    etcd = etcd3.client(host="127.0.0.1", port=2379)

    etcd.put("/test/key1", "hey key1")
    etcd.put("/test/key2", "hey key2")

    keys = list(etcd.get_prefix("/test"))

    assert keys[0][0].decode("utf-8") == "hey key1"
    assert keys[1][0].decode("utf-8") == "hey key2"
