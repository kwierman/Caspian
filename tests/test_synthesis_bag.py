from caspian.synthesis.bag import sparse_bag

def test_sparse_bag():
    db = sparse_bag(n_samples = 10000,n_cols=100)

    n_samples = db.count().compute()

    assert(n_samples == 10000)

    # now make sure that every row 

    n_records = db.map(lambda x: len(x))

    min_ = n_records.min().compute()
    max_ = n_records.max().compute()

    assert(min_ >= 1)
    assert(max_ <= 100)