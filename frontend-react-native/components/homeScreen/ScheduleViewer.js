// Home Screen Schedule Viewer Component
import React from 'react'
import { StyleSheet, View, Text } from 'react-native'

// Schedule Viewer Component
export default function ScheduleViewer() {
    return(
        <View style={styles.container}>
            <Text style={styles.schedule}>Schedule:</Text>

            {/* This coode needs to be simplified to accept data */}
            <View style={styles.line}></View>
            <Text style={styles.days}>SUNDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>MONDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>TUESDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>WEDNESDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>THURSDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>FRIDAY: </Text>
            <View style={styles.line}></View>
            <Text style={styles.days}>SATURDAY: </Text>
            <View style={styles.line}></View>

        </View>
    )
}

// Schedule Viewer Style
const styles = StyleSheet.create({
    container: {
        backgroundColor: 'white',
        height: '59%',
        borderRadius: 10,
        marginTop: 20,
        marginHorizontal: 20,
        shadowOpacity: .30,
        shadowRadius: 2,
        shadowOffset: {
            height: 0, 
            width: 1
        },
    },
    schedule: {
        color: '#99a29b',
        textAlign: 'center',
        paddingTop: 15,
        fontSize: 28,
        fontWeight: '700',
    },
    line: {
        borderBottomColor: '#b0b7b1',
        borderBottomWidth: 1,
        paddingTop: 15,
        marginHorizontal: 20,
    },
    days: {
        color: '#89938a',
        paddingLeft: 20,
        paddingTop: 15,
        fontSize: 14,
        fontWeight: '600',
    }
}) 