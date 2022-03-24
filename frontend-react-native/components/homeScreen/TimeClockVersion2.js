// Home Screen Time Clock Component
import React from 'react'
import { StyleSheet, View, Text, TouchableOpacity, Modal } from 'react-native'
import { useState } from 'react';

// Get Current Time
const getCurrentTime=()=>{
    var hour = new Date().getHours();
    var minute = new Date().getMinutes();
    if(minute == 0) {
        return hour + ':00' + 'am';
    } else if (minute > 0 && minute < 10) {
        return hour + ':0' + minute + 'am';
    } else {
        return hour + ':' + minute + 'am';
    }
}

// Time Clock Component
export default function TimeClock() {
    // Confirmation Pop-Up State
    const [confirmVisible, setConfirmVisible] = useState(false);
    return(

        // Container
        <View style={styles.container}>
            
            {/* Status Container */}
            <View style={styles.statusContainer}>

                <View style={styles.userEmblem}>
                    <View style={styles.statusIndicator}></View>
                    <Text style={styles.userInitials}>TG</Text>
                </View>
                <Text style={styles.statusText}>Status: </Text>
                <Text style={styles.status}>Clocked Out </Text>

            </View>
            
            {/*  Clock-In Button */}
            <TouchableOpacity onPress={() => setConfirmVisible(true)}>

                <View style={styles.clockInButton}>
                    <Text style={styles.clockInButtonText}>Clock In</Text>
                </View>

            </TouchableOpacity>
            
            {/* Confirmation Pop-Up */}
            <Modal
                animationType="slide"
                transparent={true}
                visible={confirmVisible}
                onRequestClose={() => {
                    Alert.alert("Modal has been closed.");
                    setModalVisible(!confirmVisible);
                }}
            >
                <View style={styles.centeredView}>

                    {/* Pop-Up Container */}
                    <View style={styles.confirmView}>
                        
                        <Text style={styles.slideText}>Confirm Clock In:</Text>
                        <View style={styles.timeTextContainer}>
                            <Text style={styles.timeText}>{getCurrentTime()}</Text>
                        </View>
                        
                        {/* Confirmation Button Container */}
                        <View style={styles.confirmButtonContainer}>
                            {/* Cancel Button */}
                            <TouchableOpacity
                                style={styles.slideButton}
                                onPress={() => setConfirmVisible(!confirmVisible)}
                            >
                                <Text style={styles.slideButtonText}>Cancel</Text>
                            </TouchableOpacity>
                            {/* Confirm Clock-In Button */}
                            <TouchableOpacity
                                style={styles.slideButton}
                                onPress={() => setConfirmVisible(!confirmVisible)}
                            >
                                <Text style={styles.slideButtonText}>Clock In</Text>
                            </TouchableOpacity>
                        </View>
                    </View>
                </View>
            </Modal>

        </View>
    )
}

// Time Clock Style
const styles = StyleSheet.create({
    container: {
        backgroundColor: 'white',
        height: 150,
        borderRadius: 10,
        marginHorizontal: 20,
        shadowOpacity: .30,
        shadowRadius: 2,
        shadowOffset: {
            height: 0, 
            width: 1
        },
    },
    statusContainer: {
        flexDirection: 'row',
        marginTop: 5,
    },
    userEmblem: {
        backgroundColor: '#f56423',
        width: 50,
        height: 50,
        borderRadius: 50,
        marginLeft: 25,
        marginVertical: 10,
    },
    statusIndicator: {
        backgroundColor: 'white', // #2ac725 green color 
        width: 15,
        height: 15,
        borderColor: '#99a29b',
        borderRadius: 50,
        borderWidth: 1,
    },
    userInitials: {
        color: 'white',
        textAlign: 'center',
        fontSize: 20,
        fontWeight: '500',
    },
    statusText: {
        color: '#99a29b',
        paddingVertical: 20,
        paddingLeft: 15,
        fontSize: 24,
        fontWeight: '700',
    },
    status: {
        color: '#f56423',
        marginVertical: 20,
        marginLeft: 5,
        fontSize: 24,
        fontWeight: '700',
    },
    clockInButton: {
        backgroundColor: '#f56423',
        height: 40,
        justifyContent: 'center',
        flex: 0,
        borderRadius: 20,
        marginHorizontal: 20,
        marginVertical: 10,
    },
    clockInButtonText: {
        color: 'white',
        textAlign: 'center',
        fontSize: 20,
        fontWeight: 'bold',
    },

    // Pop-Up Style
    centeredView: {
        justifyContent: "center",
        alignItems: "center",
        flex: 1,
        marginTop: 22,
    },
    confirmView: {
        backgroundColor: "white",
        height: '25%',
        alignItems: "center",
        position: 'absolute',
        bottom: 0,
        left: 0,
        right: 0,
        borderRadius: 20,
        padding: 15,
        shadowColor: "#000",
        shadowOpacity: 0.25,
        shadowRadius: 4,
        shadowOffset: {
          width: 0,
          height: -1
        },
    },
    slideText: {
        color: '#f56423',
        fontSize: 24,
        fontWeight: '700',
    },
    timeTextContainer: {
        justifyContent: 'center',
        width: '50%',
        height: '40%', 
    },
    timeText: {
        color: '#99a29b',
        textAlign: 'center',
        fontSize: 48,
        fontWeight: '800',
    },
    confirmButtonContainer: {
        flexDirection: 'row', 
    },
    slideButton: {
        backgroundColor: '#f56423',
        justifyContent: 'center',
        width: '50%',
        height: '58%',
        margin: 5,
        borderRadius: 20,
    },
    slideButtonText: {
        color: "white",
        textAlign: "center",
        fontSize: 20,
        fontWeight: "bold",
    },
}) 