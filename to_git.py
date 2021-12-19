def get_max_entity_id(entity):
    # max_entity_id = db.session.query(db.func.max(entity.id)).scalar() + 1
    # Orginal
    # Below is my workaround

    try:
        z = db.session.execute("select id from " + entity.__tablename__ + " order by id DESC limit 1").fetchone()
        try:
            max_entity_id = z['id']
        except:
            max_entity_id = 0
            # pass
    # except TypeError:
    except:
        max_entity_id = 0

    max_entity_id += 1
    return max_entity_id
