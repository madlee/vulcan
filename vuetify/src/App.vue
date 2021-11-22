<template>
  <v-app id="inspire">
    <v-app-bar app>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Vulcan</v-toolbar-title>
      <v-breadcrumbs
        divider="/"
        :items="path"
      ></v-breadcrumbs>
    </v-app-bar>

    <v-navigation-drawer
      v-model="drawer"
      fixed
      temporary
    >
      <!--  -->
    </v-navigation-drawer>
    
    <v-main class="grey lighten-2">
      <v-container>
        <v-row>
          <v-col
            v-for="j in folders"
            :key="`dir-${j.name}`"
            cols="6"
            md="2"
          >
            <a @click="chdir(j)">
              <v-img
                max-height="150"
                max-width="250"
                src="./assets/folder.jpg"
              ></v-img>
              <p><strong>{{ j.name }}</strong></p>
            </a>
          </v-col>
        </v-row>

        <v-row>
          <v-col
            v-for="j in images"
            :key="`img-${j.name}`"
            cols="6"
            md="2"
          >
            <a @click="show_image(j)">
              <v-img
                lazy-src="https://picsum.photos/id/11/10/6"
                max-height="150"
                max-width="250"
                src="https://picsum.photos/id/11/500/300"
              ></v-img>
              <p><strong>{{ j }}.png</strong></p>
            </a>
          </v-col>
        </v-row>
        
        <v-dialog
          v-model="dialog"
          fullscreen
          hide-overlay
          transition="dialog-bottom-transition"
        >
          <v-card>
            <v-toolbar
              dark
              color="primary"
            >
              <v-btn
                icon
                dark
                @click="dialog = false"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-toolbar-title>{{active_image}}.png</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-toolbar-items>
                
              </v-toolbar-items>
            </v-toolbar>
            <v-img></v-img>

            
          </v-card>
        </v-dialog>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    data: () => (
      { 
        drawer: null , 
        path: [],
        dialog: false,
        active_image: '',
        big_url: '',
        folders: [],
        images: []
      }
    ),
    methods: {
      show_image(img_name) {
        this.active_image = img_name
        this.dialog = true
      },
      chdir(dir) {
        let target = []
        for (var i = 1; i < this.path.length; ++i) {
          target.push(this.path[i].text)
        }
        target.push(dir.name)
        console.log(target)
        this.load_folder(target.join('/'))
      },
      load_folder(path) {
        let self = this
        this.axios
          .get('http://127.0.0.1:8000/vulcan/'+ 'list.json?path='+path)
          .then(function(response) {
            self.path = [{'text': 'Root'}]
            let path = response.data.path.split('/')
            for (var i = 0; i < path.length; ++i) {
              if (path[i].length > 0) {
                self.path.push({'text': path[i]})
              }
            }
            self.folders = response.data.folders
            self.images = response.data.images
          })
      }
    }, 
    mounted() {
      this.load_folder('')
      
    }
  }
</script>
