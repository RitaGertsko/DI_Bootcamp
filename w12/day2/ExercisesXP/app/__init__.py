from flask import Flask

my_app = Flask(__name__)

my_app.config['SECRET_KEY'] = '2bba1816323af11d20b9635072f450e8e07c8f7e31bdfa1f5fd9837a3c28b076eacdf22166854deb75e56ff35f5290f7e2f82d209be6aed2b96e083984a993a77d35955b3637322cbbc81f7e62008eb2a3c93734e7dda0a50ca72785d59173c1c4b7f7a2f99179d4767ee9dae855c6c395685454bf5e4f67b6d3f9e1e8f228171de8f14e421fb67d0077b6d1ea4308a6505b430c5826c1cbbf0f2504cca9bb8a8a3d80d931099e6ab7742da9d1ca3e6313d578df1b769f9abd5b6cbad41ecfacc68215bec61b9abd157313201534158e761da4aea786b6e4658c7951c9f99e72f1b76e1acbcc4d4982fc136544034747df4cf6cb8f5da5f1cdff4a8261ede11c'

from app import routes, forms
