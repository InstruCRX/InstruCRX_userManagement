<template>
<body>
  <div>
    <!-- layout prior exercise: prompts user to login -->
    <div class="is-vhcentered has-text-centered pt-6" style="height: 100%">
      <img class="image is-hcentered" style="width: 100px" src="./assets/iceberg.png" />

      <div class="is-json title mt-6 pt-6" v-if="!(gameCompleted && showFlagSubmission)">
        Welcome to {{scenarioName}}.
        <div class="subtitle mb-6">A Cyber Range for Incident Response Training.</div>
        <div
          class="title has-text-primary is-json mb-6"
          v-if="userRegistered"
        >GroupID: {{this.userID}}</div>
      </div>

      <div class="is-json title margin-big" v-if="gameCompleted && showFlagSubmission">
        Congrats, you finished.
        <div class="subtitle mb-6">
          There is nothing more to do here. Click the
          <strong class="has-text-primary">Finish Game</strong> button in you training environment.
        </div>
      </div>

      <div class="margin-big has-text-centered">
        <div v-if="!userRegistered">
          <form @submit.prevent="validateId()" v-if="!VMAssigned">
            <div class="field is-hcentered">
              <span>
                <input
                  class="input input-label-short is-size-6"
                  :value="'Your '+ group_naming + ': '"
                />
                <!-- Change Back -->
              </span>
              <span>
                <input
                  class="input input-short is-size-6 blank-input"
                  v-model="userID"
                  :placeholder="group_namingPlaceholder"
                />
              </span>
            </div>
            <div class="has-text-danger" v-if="emptyInput">Group ID cannot be empty.</div>
            <div class="has-text-danger" v-if="VMsTaken">
              No free Cyber Range environments at the moment.
              <br />Please contact one of the trainers.
            </div>

            <br />
            <br />
            <div class="buttons is-centered" v-if="!(VMAssigned || userExists)">
              <button
                class="button submit-button is-rounded is-large"
                type="submit"
                value="Submit"
                @click="validateId()"
                v-if="!VMsTaken"
              >
                <span>Login</span>
              </button>
            </div>
          </form>
        </div>
        <div></div>
      </div>
      <div
        class="title pt-6"
        v-if="userRegistered && !showFlagSubmission && !showTraining && !groupMembersRegistered"
      >
        Hello
        <strong class="has-text-primary">{{ this.userPseudonym }}</strong>.
        <div
          class="small subtitle"
        >This will be your group name on the cyber range. Good to have you guys here!</div>
        <br />
        <div class="small subtitle">Please register the three team members</div>

        <form @submit.prevent="registerGroupMembers()" class="mt-5" v-if="!groupMembersRegistered">
          <div class="columns is-offset-one-quarter">
            <input
              class="input input-label-short is-size-6 is-centered column"
              :value="'Group member 1'"
            />
            <!-- Change Back -->
            <span>
              <input
                class="input is-size-6 blank-input column"
                v-model="groupMemberOne"
                :placeholder="'djf73942'"
              />
            </span>
          </div>

          <div class="columns is-offset-one-quarter">
            <input
              class="input input-label-short is-size-6 is-centered column"
              :value="'Group member 2'"
            />
            <!-- Change Back -->
            <span>
              <input
                class="input is-size-6 blank-input column"
                v-model="groupMemberTwo"
                :placeholder="'glm09479'"
              />
            </span>
          </div>

          <div class="columns is-offset-one-quarter">
            <input
              class="input input-label-short is-size-6 is-centered column"
              :value="'Group member 3'"
            />
            <!-- Change Back -->
            <span>
              <input
                class="input is-size-6 blank-input column"
                v-model="groupMemberThree"
                :placeholder="'dlr72540'"
              />
            </span>
          </div>
          <div
            class="has-text-danger is-size-5"
            v-if="emptyGroupMembers"
          >Group member fields cannot be empty.</div>

          <div class="buttons is-centered">
            <button
              class="button submit-button is-rounded is-large mt-5"
              type="submit"
              value="Submit"
              @click="registerGroupMembers()"
            >
              <span>Register Group Members</span>
            </button>
          </div>
        </form>
      </div>

      <div
        class="buttons is-centered pt-6"
        v-if="userRegistered && groupMembersRegistered && !showFlagSubmission && !showTraining"
      >
        <button
          class="button submit-button is-rounded is-large"
          type="submit"
          value="Submit"
          @click="
                //proceedToQuiz();
                quizStarted = true;
                showTraining=true;
              "
        >
          <span>Go To Cyber Range Training &#10140;</span>
        </button>

        <button
          class="button is-rounded is-large"
          type="submit"
          value="Submit"
          @click="
                //proceedToQuiz();
                showFlagSubmission = true;
              "
        >
          <span>Go To Flag Submission Dashboard &#10140;</span>
        </button>
      </div>

      <div v-if="quizCompleted">
        <div class="buttons is-centered mt-5">
          <button
            class="button submit-button is-rounded mt-5 is-large"
            type="submit"
            value="Submit"
            @click="proceedToCR()"
          >
            <span>Proceed To Cyber Range →</span>
          </button>
        </div>
      </div>

      <div v-if="quizActivated && quizStarted && !quizCompleted ">
        <div v-if="!quizCompleted" class="mb-6">
          <div class="subtitle">
            Before starting with the cyber range training, please take part in our pre-quiz.
            <br />Please use your
            <strong class="title">{{naming}} ({{namingPlaceholder}})</strong>
            to
            register for the quiz.
          </div>

          <div class="buttons is-centered pt-6" v-if="!quizStarted && showTraining">
            <button
              class="button submit-button is-rounded is-large"
              type="submit"
              value="Submit"
              @click="
                //proceedToQuiz();
                quizStarted = true;
              "
              v-if="!VMsTaken"
            >
              <span>Start Quiz &#10140;</span>
            </button>
          </div>

          <iframe
            v-if="quizStarted"
            :src="urlPreQuiz"
            style="display: block; width: 100%; height: 50vh"
            class="pt-6"
          ></iframe>

          <!--iframe
            src="https://docs.google.com/forms/d/e/1FAIpQLSc2GrvpCAjUWFmrYaphlf5BCWi48b8VICbI6a-9HOUFh3LOqg/viewform?embedded=true"
            width="640"
            height="606"
            frameborder="0"
            marginheight="0"
            marginwidth="0"
          >Wird geladen…</iframe-->

          <div v-if="quizStarted" class="mt-5">
            Nothing to see? Click
            <strong>
              <a class="has-text-link" :href="urlPreQuiz" target="_blank">
                <u>here</u>
              </a>
            </strong> and come back to this page when you have finished.
          </div>

          <br />

          <div class="is-4">
            <strong>Disclaimer:</strong>
            By answering the evaluation questions, you agree that your data may be used
            <strong>anonymized</strong> for research purposes at the University of Regensburg.
            It is guaranteed that all data will be anonymized and securely stored in accordance with the European General Data Protection Regulation (DSGVO/GDPR) and that only those responsible for the research will have access to the data. All data will be used exclusively for research purposes and will not be passed on to third parties. You can withdraw your consent at any time.
          </div>
          <br />

          <div class="buttons is-centered pt-6" v-if="quizStarted">
            <button
              class="button submit-button is-rounded is-large"
              type="submit"
              value="Submit"
              @click="quizCompleted = true"
              v-if="!VMsTaken"
            >
              <span>Quiz Completed &#10004;</span>
            </button>
          </div>
        </div>
      </div>

      <div v-if="quizCompleted && VMAssigned">
        <br />Thank you for registration. We registered your user ID
        <strong
          class="has-text-primary"
        >{{ this.userID }}</strong>
        and set
        up the cyber range for you.
      </div>

      <br />
      <div v-if="!gameCompleted">
        <div :style="{width: '700px'}">
          <div v-if="showFlagSubmission">
            <div v-if="userRegistered">
              <div id="identOne">
                <flag-submission
                  :taskData="Unit1IdentTasks"
                  :order="this.order"
                  :tasksCompleted="tasksCompleted"
                  :userPseudonym="this.userPseudonym"
                  :userLevel="this.level"
                  @submit-points="submitPoints"
                  @task-completed="markAsCompleted"
                  @ident-one-completed="this.startRespOne = true"
                  @get-marker="getUserPoints"
                ></flag-submission>
              </div>
              <div id="identTwo">
                <flag-submission
                  :taskData="Unit2IdentTasks"
                  :order="this.order"
                  :tasksCompleted="tasksCompleted"
                  :userPseudonym="this.userPseudonym"
                  :userLevel="this.level"
                  @submit-points="submitPoints"
                  @task-completed="markAsCompleted"
                  @ident-two-completed="this.startRespTwo = true"
                  @get-marker="getUserPoints"
                  v-if="this.level>=2"
                ></flag-submission>
              </div>
              <div id="respTwo">
                <flag-submission
                  :taskData="Unit2RespTasks"
                  :order="this.order"
                  :tasksCompleted="tasksCompleted"
                  :userPseudonym="this.userPseudonym"
                  :userLevel="this.level"
                  @submit-points="submitPoints"
                  @task-completed="markAsCompleted"
                  @game-finished="this.gameCompleted=true"
                  @get-marker="getUserPoints"
                  v-if="this.level>=4"
                ></flag-submission>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <nav class="navbar is-fixed-bottom is-transparent mb-1" v-if="showFlagSubmission">
    <div class="navbar-brand navbar-background is-half">
      <div class>
        <!-- implementation of the scoreboard -->
        <div class="navbar-brand" v-if="!hideScoreboard">
          <table class="table is-size-10 has-text-white dashboard mt-1 mb-1" width="100%">
            <tbody class="pt-5 has-text-white">
              <tr class="has-text-white">
                <th class="has-text-white">Rank</th>
                <th class="has-text-white">Username</th>
                <th class="has-text-white">Points</th>
                <th class="has-text-white">Level</th>
              </tr>
              <tr
                v-for="(item, index) in dashboard"
                :key="item"
                :class="{
                            'has-text-primary has-text-weight-bold':
                              item.userID == this.userID,
                          }"
              >
                <td>{{ index + 1 }}</td>
                <td>{{ item.pseudonym }}</td>
                <td>{{ item.points }}</td>
                <td>{{ item.level }}</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- implementation of the buttons 
                        - to hide/show the scoreboard 
                        - to enable/disable fullscreen mode for the kibana dashboard
        -->
        <div id="navbarBasicExample" class="navbar-menu">
          <div class="buttons is-left">
            <button
              class="button is-primary is-static is-small has-background-primary has-text-white"
            >
              <strong>Points: {{ points }}</strong>
            </button>

            <button class="button is-primary is-small is-static">
              <strong>Level: {{ this.level }}</strong>
            </button>
          </div>
        </div>
      </div>
    </div>
  </nav>
</body>
</template>

<script>
import { userDashboard } from "@/firebase"; // TODO rename to userScoreboard
import { VM_db } from "@/firebase";
import settings from "./Settings.js";
import FlagSubmission from "./components/FlagSubmission.vue";
import Unit1IdentTasks from "./data/Unit1IdentTasks.js";
import Unit2IdentTasks from "./data/Unit2IdentTasks.js";
import Unit2RespTasks from "./data/Unit2RespTasks.js";

export default {
  name: "App",

  components: {
    FlagSubmission,
  },

  data() {
    return {
      Unit1IdentTasks: Unit1IdentTasks,
      Unit2IdentTasks: Unit2IdentTasks,
      Unit2RespTasks: Unit2RespTasks,
      gameStarted: false,
      userID: null,
      groupMemberOne: null,
      groupMemberTwo: null,
      groupMemberThree: null,
      round: null,
      points: null,
      emptyInput: false,
      emptyGroupMembers: false,
      groupMembersRegistered: false,
      inputGiven: false,
      userExists: false,
      VMData: null,
      VMAssigned: false,
      VMsTaken: false,
      dashboard: null,
      userPseudonym: null,
      blockly: null,
      ip: null,
      quizActivated: true,
      quizCompleted: false, // false if quiz activated
      quizStarted: false,
      scenarioName: settings.scenarioName,
      urlPreQuiz: settings.urlPreQuiz,
      naming: settings.naming,
      namingPlaceholder: settings.namingPlaceholder,
      group_naming: settings.group_naming,
      group_namingPlaceholder: settings.group_namingPlaceholder,
      userRegistered: false,
      showTraining: false,
      showFlagSubmission: false,
      order: ["unit1Ident", "unit2Ident", "unit2Resp"],
      level: null,
    };
  },

  computed: {
    gameCompleted() {
      if (this.level == 8) {
        return true;
      } else {
        return false;
      }
    },
  },

  methods: {
    proceedToCR() {
      this.url = "http://" + this.ip + ":7080?userID=" + this.userID;
      console.log(this.url);

      console.log(this.url);
      window.open(this.url, "_self");
    },

    registerGroupMembers() {
      if (
        this.groupMemberOne == null ||
        this.groupMemberTwo == null ||
        this.groupMemberThree == null
      ) {
        this.emptyGroupMembers = true;
      } else {
        this.emptyGroupMembers = false;
        userDashboard.doc(this.userID).update({
          groupMemberOne: this.groupMemberOne,
          groupMemberTwo: this.groupMemberTwo,
          groupMemberThree: this.groupMemberThree,
        });
        this.groupMembersRegistered = true;
      }
    },

    validateId() {
      if (this.userID == null) {
        this.userExists = false;
        this.emptyInput = true;
      } else {
        this.emptyInput = false;
        this.inputGiven = true;
        this.userExists = false;
        this.assignVM();
      }
    },

    //randomly retrieve combination of yet unassigned VM/pseudonym
    //create link for user, store userID in localStorage

    assignVM() {
      //create document in user database (cyberrangeDashboard)
      var docRef = userDashboard.doc(String(this.userID));
      docRef.get().then((doc) => {
        if (doc.exists) {
          //check if pseudonym was used before
          this.userExists = true;
          this.getVM();
        } else {
          //register user
          this.getFreeVM();
        }
      });
    },

    async getFreeVM() {
      const snapshot = await VM_db.where("userID", "==", "").limit(1).get();

      this.VMData = snapshot.docs.map((doc) => doc.data());

      if (typeof this.VMData[0] !== "undefined") {
        this.ip = this.VMData[0].ip;
        var blockBool = this.VMData[0].blockly === "true";

        this.blockly = blockBool;

        //const check = await VM_db.doc(this.ip).get();
        //console.log("still empty: ", check.data().userID)

        VM_db.doc(this.ip).update({
          userID: this.userID,
        });

        userDashboard.doc(this.userID).set({
          round: this.VMData[0].round,
          level: 0,
          points: 0,
          ip: this.VMData[0].ip,
          pseudonym: this.VMData[0].pseudonym,
          userID: this.userID,
        });

        this.userPseudonym = this.VMData[0].pseudonym;

        //this.url="http://localhost:7080?userID="+this.userID;

        this.VMAssigned = true;
        this.userRegistered = true;
      } else {
        this.VMsTaken = true;
      }
    },

    async getVM() {
      var docRef = userDashboard.doc(String(this.userID));
      docRef
        .get()
        .then((doc) => {
          if (doc.exists) {
            this.getUserPoints();
            //in order to only show the trainees from the same round on the dashboard
            //get data from user who logged in before
          }
          this.userRegistered = true;
          this.getMarker();
        })
        .catch((error) => {
          console.log("Error getting document:", error);
        });
    },

    getUserPoints() {
      var docRef = userDashboard.doc(String(this.userID));

      docRef
        .get()
        .then((doc) => {
          if (doc.exists) {
            this.round = doc.data().round; //in order to only show the trainees from the same round on the dashboard
            if (doc.data().startTime != null) {
              //get data from user who logged in before
              console.log("found it");
              this.points = doc.data().points;
              this.level = doc.data().level;
              this.startTime = doc.data().startTime;
              this.userPseudonym = doc.data().pseudonym;
              this.ip = doc.data().ip;

              if (this.level > 4) {
                this.playbookTwoBegin = true;
              }
              if (doc.data().taskTimes != null) {
                this.taskTimes = JSON.parse(doc.data().taskTimes);
              }
            } else {
              //registered player who didn't log in before
              console.log(doc.data().startTime);
              this.level = 0;
              this.startTime = new Date();
              this.userPseudonym = doc.data().pseudonym;
              this.ip = doc.data().ip;
              userDashboard.doc(this.userID).update({
                startTime: this.startTime,
              });

              var storedTries = [3, 3, 3, 3, 3, 3, 3, 3];
              var blanksCompleted = {
                unit1Ident: 0,
                unit2Ident: 0,
                unit2Resp: 0,
              };
              localStorage.setItem("storedTries", JSON.stringify(storedTries));
              localStorage.setItem(
                "blanksCompleted",
                JSON.stringify(blanksCompleted)
              );
            }
          } else {
            // if not only played with preset users
            this.points = 0;
            this.level = 0;
            this.startTime = new Date();
            userDashboard.doc(this.userID).set({
              startTime: this.startTime,
              round: 1,
              level: 0,
              points: 0,
            });
          }

          if (doc.data().groupMemberOne != null) {
            this.groupMembersRegistered = true;
          }

          this.getMarker();
        })
        .catch((error) => {
          console.log("Error getting document:", error);
        });
    },

    async getMarker() {
      const snapshot = await userDashboard
        .where("round", "==", this.round)
        .orderBy("points", "desc")
        .get();
      //const snapshot = await userDashboard.orderBy("points", "desc").get();
      this.dashboard = snapshot.docs.map((doc) => doc.data());
    },

    submitPoints(points2) {
      this.points += points2;
      console.log("points now: ", this.points);
      if (points2 >= 0) {
        this.level += 1;
        console.log(this.mitmRunning);
      }

      this.uploadPoints();
    },

    async uploadPoints() {
      await userDashboard.doc(this.userID).update({
        points: this.points,
        level: this.level,
        startTime: this.startTime,
      });
      this.getMarker();
    },

    async uploadEvaluationData() {
      await userDashboard.doc(this.userID).update({
        taskTimes: JSON.stringify(this.taskTimes),
        tries: JSON.stringify(this.tries),
      });
    },

    /*   async uploadPoints() {
      await userDashboard.doc(this.userID).update({
        points: this.points,
        level: this.tasksCompleted,
        startTime: this.startTime,
      });
      this.getMarker();
    },

    async uploadEvaluationData() {
      await userDashboard.doc(this.userID).update({
        taskTimes: JSON.stringify(this.taskTimes),
      });
    },

*/
  },
};
</script>

<style>
@import "./../css/bulma.css";
@import "./../css/bulma-tooltip.css";
</style>
