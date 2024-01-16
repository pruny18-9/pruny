from flask import Flask, request, jsonify
from config import icebox_config as conf
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from datetime import datetime
import logging

DATABASE_URI = f'mysql+pymysql://{conf.user}:{conf.passwd}@{conf.host}:{conf.port}/{conf.dbname}'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 객체의 수정을 추적하지 않습니다.
CORS(app)

engine = create_engine(DATABASE_URI)
metadata = MetaData()
Base = automap_base()
Base.prepare(engine, reflect=True)

# 가져온 모델 클래스들


Item = Base.classes.Item
Favorite = Base.classes.Favorite
session = Session(engine)

# for Item
@app.route('/icebox/getItemList')
def get_item_list():
    item_list = session.query(Item).all()
    data = []
    for item in item_list:
        data.append(
            {
                'id': item.id,
                'name': item.name,
                'regdate': item.regdate.strftime('%Y-%m-%d %H:%M:%S'),
                'expdate': item.expdate.strftime('%Y-%m-%d %H:%M:%S'),
                'img': item.img
            }
        )
    return jsonify({
        "data": data
    })


@app.route('/icebox/<item_id>', methods=['GET'])
def get_item(item_id):
    try:
        # 특정 id에 해당하는 Item을 찾습니다.
        item = session.query(Item).get(item_id)

        if item:
            data = {
                    'id': item.id,
                    'name': item.name,
                    'regdate': item.regdate.strftime('%Y-%m-%d %H:%M:%S'),
                    'expdate': item.expdate.strftime('%Y-%m-%d %H:%M:%S'),
                    'img': item.img
                    }
            return jsonify({
                "data": data
            })
        else:
            return jsonify({
                'error': f'id {item_id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/icebox/registItem', methods=['POST'])
def regist_item():
    try:
        # POST 요청에서 JSON 데이터 추출
        data = request.json
    
        # 새로운 아이템 생성
        new_item = Item(
            name = data.get('name', '???'),
            regdate = data.get('regdate', datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            expdate = data.get('expdate', '9999-12-31 23:59:59'),
            img = data.get('img', 'https://github.com/pruny18-9/pruny/blob/main/img/pruny.png')
        )
    
        # 데이터베이스에 추가
        session.add(new_item)
        session.commit()

        return jsonify({
            'data': f'{data.get("name")} added successfully'
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })


@app.route('/icebox/<item_id>', methods=['DELETE'])
def remove_item(item_id):
    try:
        # 특정 id에 해당하는 Item을 찾습니다.
        item = session.query(Item).get(item_id)

        if item:
            # 데이터베이스에서 삭제
            session.delete(item)
            session.commit()

            return jsonify({
                'data': f'{item.name} removed successfully'
            })
        else:
            return jsonify({
                'error': f'id {item_id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


#############################################################################################
#############################################################################################

# for favorite
@app.route('/icebox/getFavoriteList')
def get_favorite_list():
    favorite_list = session.query(Favorite).all()
    data = []
    for favorite in favorite_list:
        data.append(
            {
                'id': favorite.id,
                'name': favorite.name,
                'img': favorite.img
            }
        )
    return jsonify({
        "data": data
    })


@app.route('/icebox/<favorite_id>/favorite', methods=['GET'])
def get_favorite(favorite_id):
    try:
        # 특정 id에 해당하는 Favorite을 찾습니다.
        favorite = session.query(Favorite).get(favorite_id)

        if favorite:
            data = {
                'id': favorite.id,
                'name': favorite.name,
                'img': favorite.img
            }
            return jsonify({
                "data": data
            })
        else:
            return jsonify({
                'error': f'id {favorite_id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


@app.route('/icebox/registFavorite', methods=['POST'])
def regist_favorite():
    try:
        # POST 요청에서 JSON 데이터 추출
        data = request.json

        # 새로운 아이템 생성
        new_favorite = Favorite(
            name=data.get('name', '???'),
            img=data.get('img', 'https://github.com/pruny18-9/pruny/blob/main/img/pruny.png')
        )

        # 데이터베이스에 추가
        session.add(new_favorite)
        session.commit()

        return jsonify({
            'data': f'{data.get("name")} added successfully'
        })
    except Exception as e:
        return jsonify({
            'error': str(e)
        })


@app.route('/icebox/<favorite_id>/favorite', methods=['DELETE'])
def remove_favorite(favorite_id):
    try:
        # 특정 id에 해당하는 Favorite을 찾습니다.
        favorite = session.query(Favorite).get(favorite_id)

        if favorite:
            # 데이터베이스에서 삭제
            session.delete(favorite)
            session.commit()

            return jsonify({
                'data': f'{favorite.name} removed successfully'
            })
        else:
            return jsonify({
                'error': f'id {favorite_id} not found'
            }), 404
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
