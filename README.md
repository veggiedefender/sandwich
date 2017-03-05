# sandwich

##👉[API Docs](https://github.com/veggiedefender/sandwich/blob/master/api.md)

##setup

Follow [this guide](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04) to set up the nginx/uwsgi/flask stack.

##back end

This is a pretty straightforward flask app that mostly follows [this structure](https://github.com/pallets/flask/wiki/Large-app-how-to).

##front end

Don't try to edit the minified code found in `app/static` or `app/templates`!
Since this project is ***WEB SCALE*** it's using react and changes you make to the built assets won't be persisted the next time the code gets built.

However, there's a nice [`frontend`](https://github.com/veggiedefender/sandwich/tree/master/frontend) folder containing js and jsx code which you can edit.

Run `npm run build` to run the 🌟javascript magic🌟 which will copy the built assets into the 
right flask folders (aka it runs [`installToFlask.sh`](https://github.com/veggiedefender/sandwich/blob/master/frontend/installToFlask.sh)).

##maintaining

If you want a feature, create an issue or implement it yourself. I'll accept almost any pull request if it's any good.

If you're interested in maintaining this, contact me and I can give you push access.
